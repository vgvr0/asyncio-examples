## 1. LIBRERÍAS

El programa comienza cargando varias bibliotecas de `R` que se utilizarán en el análisis. Estas bibliotecas incluyen `doMC` para la computación paralela, `ggplot2` para la visualización de datos, `glmnet` para los modelos `Elastic Net`, `Lasso` y `Ridge`, `gridExtra` para la disposición de gráficos, `parallel` para la computación paralela, `pROC` para el análisis de curvas ROC, `randomForest` para el modelo de Random Forest, `readr` para leer archivos de datos y `tidyverse` para la manipulación de datos.

```R
library(doMC)
library(ggplot2)
library(glmnet)
library(gridExtra)
library(parallel)
library(pROC)
library(randomForest)
library(readr)
library(tidyverse)
```

Para instalar los paquetes necesarios, ejecute esta línea: 
```R
install.packages(c("doMC", "ggplot2", "glmnet", "gridExtra", "parallel", "pROC", "randomForest", "readr", "tidyverse"))
```

## 2. PREPARACIÓN DE DATOS. 

Lee un conjunto de datos de un archivo `CSV`, convierte todas las variables en factores y luego utiliza `model.matrix` para expandir y codificar las variables categóricas. Se crea `data.X` excluyendo la columna 86 (columna de la variable de respuesta, CARAVAN).
Finalmente, se crea un nuevo dataframe `data.full` que contiene todas las variables explicativas codificadas, junto con la variable de respuesta `CARAVAN`, que se agrega como una columna al final.
```R
data <- read_csv("caravan-insurance-challenge.csv") %>% as.data.frame()
data.X <- data[,-86] 
data.X <- lapply(data.X, factor)
data.X <- model.matrix(~.-1, data = data.X) 
data.Y <- as.factor(data$CARAVAN)
data.full <- as.data.frame(data.X)
data.full$CARAVAN <- data.Y
```

Se inicializan varias matrices para almacenar los resultados de las simulaciones. Estos incluyen un marco de datos para almacenar los valores `AUC` (Área bajo la curva ROC) para cada método y cada iteración, un marco de datos para almacenar los tiempos de validación cruzada para cada método y cada iteración, y un marco de datos para almacenar los valores de lambda para cada método y cada iteración.

```R
runs = 50  
auc.initialize <- rep(0, runs)
Run   = seq(1, runs)
ElNet = auc.initialize
Lasso = auc.initialize
Ridge = auc.initialize
RF    = auc.initialize
auc.df <- data.frame(Run   = Run,
                     ElNet.train = ElNet,
                     Lasso.train = Lasso,
                     Ridge.train = Ridge,
                     RF.train    = RF,
                     ElNet.test  = ElNet,
                     Lasso.test  = Lasso,
                     Ridge.test  = Ridge,
                     RF.test     = RF)
times = data.frame(Run = Run, 
                   ElNet = rep(0, runs), 
                   Lasso = rep(0, runs), 
                   Ridge = rep(0, runs),
                   RF    = rep(0, runs))
lambdas.df <- data.frame(Run = runs, 
                         ElNet = rep(0,runs),
                         Lasso = rep(0,runs),
                         Ridge = rep(0,runs))
```
Partición de entrenamiento y test: 
```R
  ##### Partición Training Data #####
  writeLines("Particionando datos Training")
  X.train = data.X[train.indices,]
  Y.train = data.Y[train.indices]
  
  writeLines("Particionando datos Test")
  X.test = data.X[test.indices,]
  Y.test = data.Y[test.indices]
```
### Validación cruzada. 

Los argumentos `X.train` y `Y.train` son los predictores y la variable de respuesta respectivamente para el conjunto de entrenamiento. Con `parallel = TRUE` se indica que el ajuste del modelo se realizará en paralelo, lo que puede acelerar el proceso en sistemas con múltiples núcleos de CPU. El ejemplo se muestra para `Elastic Net`y se realiza con todos los modelos.

`family = "binomial"` especifica que se está realizando un modelo de regresión logística para una variable de respuesta binaria. 
`alpha = elnet.alpha` especifica el parámetro de mezcla para `Elastic Net`. 
`type.measure = "auc"` indica que la métrica de evaluación utilizada durante la validación cruzada es el área bajo la curva (AUC).

```R
  # Elastic Net
  elnet.start <- proc.time()
  elnet.cv    <- cv.glmnet(X.train, Y.train,
                           parallel     = TRUE, 
                           family       = "binomial",
                           alpha        = elnet.alpha, 
                           type.measure = "auc")
  elnet.end   <- proc.time()
  elnet.time  <- elnet.end[3]-elnet.start[3]
  cat("Tarda", elnet.time, "segundos, en la iteración", i, "\n")
  times$ElNet[i]  <- elnet.time
```
## 3. RESULTADOS. 

El siguiente código se utiliza para ver el orden de importancia de las variables: 

```R
# Fuerza el gráfico para mantener el orden de importancia. 
variable.importance$Number <- factor(variable.importance$Number, levels=variable.importance$Number) 

variable.importance_ELN   <- variable.importance[order(abs(variable.importance$ElNet), decreasing = TRUE),]
variable.importance_ELN

variable.importance_L   <- variable.importance[order(abs(variable.importance$Lasso), decreasing = TRUE),]
variable.importance_L

variable.importance_R   <- variable.importance[order(abs(variable.importance$Ridge), decreasing = TRUE),]
variable.importance_R

variable.importance_RF   <- variable.importance[order(abs(variable.importance$MeanDecreaseGini), decreasing = TRUE),]
variable.importance_RF
```

Crea varios gráficos y matrices para visualizar los resultados, incluyendo gráficos de caja para los valores`AUC` y gráficos de barras para los coeficientes estandarizados de los modelos.

```R
# Crea gráficos y cuadrículas
elnetPlot = variable.importance %>% ggplot(aes(x = Number, y = ElNet)) +
  geom_bar(stat = "identity", fill="white", colour="#FF0000") +
  labs(title = "Standardized Elastic Net Coefficients", x = "Variable", y = "Coefficient") + theme(axis.title.x=element_blank(), axis.text.x=element_blank(),axis.ticks.x=element_blank())

lassoPlot = variable.importance %>% ggplot(aes(x = Number, y = Lasso))  +
  geom_bar(stat = "identity", fill="white", colour="#70AD47") +
  labs(title = "Standardized Lasso Coefficients", x = "Variable", y = "Coefficient") + theme(axis.title.x=element_blank(), axis.text.x=element_blank(),axis.ticks.x=element_blank())

ridgePlot = variable.importance %>% ggplot(aes(x = Number, y = Ridge)) +
  geom_bar(stat = "identity", fill="white", colour="#CC04C2") +
  labs(title = "Standardized Ridge Coefficients", x = "Variable", y = "Coefficient") + theme(axis.title.x=element_blank(), axis.text.x=element_blank(),axis.ticks.x=element_blank())

rfPlot = variable.importance %>% ggplot(aes(x = Number, y = MeanDecreaseGini)) +
  geom_bar(stat = "identity", fill="white", colour="#02C9CE") +
  labs(title = "Random Forrest Variable Importance", x = "Variable", y = "Importance") + theme(axis.title.x=element_blank(), axis.text.x=element_blank(),axis.ticks.x=element_blank() )
```
