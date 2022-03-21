import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#C:\Users\USer\Desktop1\XLSXPython
data = pd.read_excel (r'C:\Users\USer\Desktop1\XLSXPython\AADAT.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
df_Time = pd.DataFrame(data, columns= ['Time'])
df_Date = pd.DataFrame(data, columns= ['Date'])
df_ini_pos1 = pd.DataFrame(data, columns= ['ini_pos1'])
df_ini_pos2 = pd.DataFrame(data, columns= ['ini_pos2'])
df_Fin_LDR1 = pd.DataFrame(data, columns= ['Fin_LDR1'])
df_Fin_LDR2 = pd.DataFrame(data, columns= ['Fin_LDR2'])
df_Fin_LDR3 = pd.DataFrame(data, columns= ['Fin_LDR3'])
df_Fin_LDR4 = pd.DataFrame(data, columns= ['Fin_LDR4'])
#VIn_AADAT
#VIn_fixed
#realV_AADAT(mV)
#realV_fixed(mV)
#C_AADAT(mA)
#C_fixed(mA)
#P_AADAT
#P_fixed
df_VIn_AADAT = pd.DataFrame(data, columns= ['VIn_AADAT'])
df_VIn_fixed = pd.DataFrame(data, columns= ['VIn_fixed'])
df_realV_AADAT = pd.DataFrame(data, columns= ['realV_AADAT'])
df_realV_fixed = pd.DataFrame(data, columns= ['realV_fixed'])
df_C_AADAT = pd.DataFrame(data, columns= ['C_AADAT'])
df_C_fixed = pd.DataFrame(data, columns= ['C_fixed'])
df_P_AADAT = pd.DataFrame(data, columns= ['P_AADAT'])
df_P_fixed = pd.DataFrame(data, columns= ['P_fixed'])
#print(df_Time)

#print (df)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/time")
def time():
    return df_Time.to_json(orient='records')

@app.get("/date")
def date():
    return df_Date.to_json(orient='records')

@app.get("/ini_pos1")
def ini_pos1():
    return df_ini_pos1.to_json(orient='records')

@app.get("/ini_pos2")
def ini_pos2():
    return df_ini_pos2.to_json(orient='records')

@app.get("/Fin_LDR1")
def Fin_LDR1():
    return df_Fin_LDR1.to_json(orient='records')

@app.get("/Fin_LDR2")
def Fin_LDR2():
    return df_Fin_LDR2.to_json(orient='records')

@app.get("/Fin_LDR3")
def Fin_LDR3():
    return df_Fin_LDR3.to_json(orient='records')

@app.get("/Fin_LDR4")
def Fin_LDR4():
    return df_Fin_LDR4.to_json(orient='records')

@app.get("/VIn_AADAT")
def VIn_AADAT():
    return df_VIn_AADAT.to_json(orient='records')

@app.get("/VIn_fixed")
def VIn_fixed():
    return df_VIn_fixed.to_json(orient='records')

@app.get("/realV_AADAT")
def realV_AADAT():
    return df_realV_AADAT.to_json(orient='records')

@app.get("/realV_fixed")
def realV_fixed():
    return df_realV_fixed.to_json(orient='records')

@app.get("/C_AADAT")
def C_AADAT():
    return df_C_AADAT.to_json(orient='records')

@app.get("/C_fixed")
def C_fixed():
    return df_C_fixed.to_json(orient='records')

@app.get("/P_AADAT")
def P_AADAT():
    return df_P_AADAT.to_json(orient='records')

@app.get("/P_fixed")
def P_fixed():
    return df_P_fixed.to_json(orient='records')