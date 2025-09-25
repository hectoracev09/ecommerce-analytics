
# =====================================================
# Proyecto: Análisis de Ventas E-commerce
# Dataset: ecommerce_sales.csv
# Autor: Héctor Acevedo
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# --- Rutas seguras relativas al proyecto ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"
IMG_DIR = PROJECT_ROOT / "images"
IMG_DIR.mkdir(parents=True, exist_ok=True)  # crea /images si no existe

# 1. Cargar dataset
df = pd.read_csv(r"C:\Users\hecto\Downloads\ecommerce_project_full\data\ecommerce_sales.csv")

# --- EDA rápida ---
print("Primeras filas del dataset:")
print(df.head())

print("\nInformación general del dataset:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

# --- KPIs ---
ventas_totales = df["Sales"].sum()
ganancia_total = df["Profit"].sum()
pedidos_totales = df["Order ID"].nunique()
clientes_totales = df["Customer ID"].nunique()
ticket_promedio = ventas_totales / pedidos_totales

print(f"\n📊 Ventas Totales: ${ventas_totales:,.2f}")
print(f"💰 Ganancia Total: ${ganancia_total:,.2f}")
print(f"📦 Pedidos Totales: {pedidos_totales}")
print(f"👥 Clientes Totales: {clientes_totales}")
print(f"💳 Ticket Promedio: ${ticket_promedio:,.2f}")

# --- Gráficos ---
# 1) Ventas por categoría
plt.figure(figsize=(8,5))
ventas_categoria = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
sns.barplot(x=ventas_categoria.values, y=ventas_categoria.index)
plt.title("Ventas Totales por Categoría")
plt.xlabel("Ventas Totales"); plt.ylabel("Categoría")
plt.tight_layout()
plt.savefig(IMG_DIR / "ventas_por_categoria.png")
plt.close()

# 2) Ventas por región
plt.figure(figsize=(8,5))
ventas_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
sns.barplot(x=ventas_region.index, y=ventas_region.values)
plt.title("Ventas Totales por Región")
plt.xlabel("Región"); plt.ylabel("Ventas Totales")
plt.tight_layout()
plt.savefig(IMG_DIR / "ventas_por_region.png")
plt.close()

# 3) Tendencia mensual
df["Order Date"] = pd.to_datetime(df["Order Date"])
ventas_mensuales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
plt.figure(figsize=(10,6))
ventas_mensuales.index = ventas_mensuales.index.astype(str)
plt.plot(ventas_mensuales.index, ventas_mensuales.values, marker="o")
plt.title("Tendencia de Ventas Mensuales")
plt.xlabel("Mes"); plt.ylabel("Ventas Totales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(IMG_DIR / "tendencia_ventas_mensuales.png")
plt.close()

# 4) Top 10 productos
plt.figure(figsize=(10,6))
top_productos = df.groupby("Product ID")["Sales"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_productos.values, y=top_productos.index)
plt.title("Top 10 Productos más Vendidos")
plt.xlabel("Ventas Totales"); plt.ylabel("Product ID")
plt.tight_layout()
plt.savefig(IMG_DIR / "top10_productos.png")
plt.close()

print("\n✅ Gráficos guardados en:", IMG_DIR)
