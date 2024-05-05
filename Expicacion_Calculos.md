## 1. LIBRERÍAS

El programa comienza cargando varias bibliotecas de `R` que se utilizarán en el análisis. Estas bibliotecas incluyen `doMC` para la computación paralela, `ggplot2` para la visualización de datos, `glmnet` para los modelos `Elastic Net`, `Lasso` y `Ridge`, `gridExtra` para la disposición de gráficos, `parallel` para la computación paralela, `pROC` para el análisis de curvas `ROC`, randomForest para el modelo de `Random Forest`, `readr` para leer archivos de datos y `tidyverse` para la manipulación de datos.

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

Lee un conjunto de datos de un archivo `CSV`, convierte todas las variables en factores y luego utiliza `model.matrix` para expandir y codificar las variables categóricas.
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

## 3. RESULTADOS. 

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
