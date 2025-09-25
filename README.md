# 🛒 Análisis de Ventas E-commerce

Este proyecto analiza un dataset simulado de **ventas en línea** con el objetivo de obtener métricas de negocio relevantes y visualizarlas mediante **Python y Power BI**.

---

## 📂 Dataset

El dataset `ecommerce_sales.csv` contiene **500 registros** de ventas con las siguientes columnas:

- **Order ID** → identificador único de pedido  
- **Customer ID** → identificador de cliente  
- **Category** → categoría del producto  
- **Sub-Category** → subcategoría del producto  
- **Product ID** → identificador único del producto  
- **Region** → ubicación del cliente  
- **Order Date** → fecha de compra  
- **Quantity** → cantidad de productos comprados  
- **Sales** → monto total de la venta  
- **Profit** → ganancia de la transacción  

---

## 🎯 Objetivo del análisis

- Calcular indicadores clave (**KPIs**) de ventas.  
- Identificar las **categorías y productos más vendidos**.  
- Analizar la **evolución temporal de las ventas**.  
- Detectar **clientes más rentables**.  
- Comparar resultados por **región**.  

---

## 📊 KPIs principales (ejemplo)

- Ventas Totales: **$628,150**  
- Ganancia Total: **$111,961**  
- Pedidos Totales: **500**  
- Clientes Totales: **99**  
- Ticket Promedio: **$1,256**  

---

## 📈 Visualizaciones

1. **Ventas por Categoría**  
   ![Ventas por Categoría](images/ventas_por_categoria.png)

2. **Ventas por Región**  
   ![Ventas por Región](images/ventas_por_region.png)

3. **Tendencia Mensual de Ventas**  
   ![Tendencia Mensual](images/tendencia_ventas_mensuales.png)

4. **Top 10 Productos más Vendidos**  
   ![Top 10 Productos](images/top10_productos.png)

---

## ⚙️ Tecnologías usadas

- **Python**: Pandas, Matplotlib, Seaborn  
- **Power BI**: dashboards interactivos  
- **GitHub**: documentación del proyecto  

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/TU_USUARIO/ecommerce-analytics.git
   cd ecommerce-analytics
   ```

2. Instalar dependencias:  
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. Ejecutar el script de análisis:  
   ```bash
   python scripts/ecommerce_analysis_base.py
   ```

4. Abrir el archivo `ecommerce_sales.csv` en Power BI para construir dashboards adicionales.

---

## 📌 Autor
👨‍💻 **Héctor Acevedo**  
Data Analytics & Business Intelligence  
[LinkedIn](https://linkedin.com/in/acevedohector09)
