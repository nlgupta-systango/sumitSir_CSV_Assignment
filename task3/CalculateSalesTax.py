import pandas as pd
import csv
import os
# Global variables

productCatalogDf = ""
salesTaxDf = ""


def uniqueNameChecker( nameList ):
    return len(nameList) == len(set(nameList))

def taxCalculation():
    if uniqueNameChecker(salesTaxDf["Country"]):
        with open("result.csv", "w", newline="") as csvFileObject:
            thewritter = csv.writer(csvFileObject)

            thewritter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

            salseTaxDfIndex = 0

            while salseTaxDfIndex < len(salesTaxDf):
                productCatalogDfIndex = 0
                while productCatalogDfIndex < len(productCatalogDf):
                    #print( type(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex]), " ", type(productCatalogDf['ProductCost'][productCatalogDfIndex]) )
                    try:
                        if( float(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex]) >= 0.0 and float(productCatalogDf['ProductCost'][productCatalogDfIndex])> 0.0):
                            taxprice = (float(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex])* float(productCatalogDf['ProductCost'][productCatalogDfIndex]))/100

                            salesprice = float(productCatalogDf['ProductCost'][productCatalogDfIndex])+taxprice
                
                            thewritter.writerow([productCatalogDf['ProductName'][productCatalogDfIndex], productCatalogDf['ProductCost'][productCatalogDfIndex], salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex], taxprice, salesprice, salesTaxDf['Country'][salseTaxDfIndex]])
                            
                        else:
                            print("input file contain invalid values")
                  
                            
                    except ValueError:
                        print("input file contain characters instead of values")
                        break;
                    except:
                        print("invalid inputs")
                        break

                    finally:
                        productCatalogDfIndex+=1

                salseTaxDfIndex+=1
    else:
        print("country name repeated")
            

        

    
def headerNameValidator():
    columnNames=["ProductName","ProductCost","SalseTaxInPercent","Country"]

    for x in productCatalogDf:
        if x not in columnNames:
            return False

    for x in salesTaxDf:
        if x not in columnNames:
            return False

    
    #print(productCatalogDf["ProductName"])
    return True



if __name__ == "__main__":
    ProductCatalogFilePath = os.path.join(".","ProductCatalog.csv")
    salesTaxFilePath = os.path.join(".","SalesTax.csv")


    if os.path.exists(ProductCatalogFilePath) and os.path.exists(salesTaxFilePath):
        print("file exist")
        
        
        productCatalogDf = pd.read_csv("ProductCatalog.csv")
        salesTaxDf = pd.read_csv("SalesTax.csv")
        
        if headerNameValidator():
            print("headers are valid")
            taxCalculation()
        else:
            print("headers are not valid")

    else:
        print("file dosen't exist")





'''
    file validations

    
    does file exist
        |
    does header are correct
        |
    does country name are repeated
'''


