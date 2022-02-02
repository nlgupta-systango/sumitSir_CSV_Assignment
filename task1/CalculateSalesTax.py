import pandas as pd
import csv

productCatalogDf = pd.read_csv("ProductCatalog.csv") #Df=dataFrame
salesTaxDf = pd.read_csv("SalesTax.csv")

with open("result.csv", "w", newline="") as csvFile:
    thewritter = csv.writer(csvFile)

    thewritter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

    salesCsvCounter= 0

    while salesCsvCounter < len(salesTaxDf):
        productCsvCounter = 0
        while productCsvCounter < len(productCatalogDf):
            taxprice = (float(salesTaxDf['SalseTaxInPercent'][salesCsvCounter])* float(productCatalogDf['ProductCost'][productCsvCounter]))/100
            salesprice = float(productCatalogDf['ProductCost'][productCsvCounter])+taxprice    
            thewritter.writerow([productCatalogDf['ProductName'][productCsvCounter], productCatalogDf['ProductCost'][productCsvCounter], salesTaxDf['SalseTaxInPercent'][salesCsvCounter], taxprice, salesprice, salesTaxDf['Country'][salesCsvCounter]])
            productCsvCounter+=1
        salesCsvCounter+=1
    print('Done ')

