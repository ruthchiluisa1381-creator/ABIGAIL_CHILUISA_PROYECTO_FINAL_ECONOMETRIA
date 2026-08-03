import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

def estimar_logit_probit(df_path):
    """Estima los modelos Logit y Probit y retorna los resultados."""
    df = pd.read_parquet(df_path)
    
    # Especifique su fórmula econométrica
    formula = "informal ~ edad + np.power(edad, 2) + C(sexo) + educacion + C(zona)"
    
    # Estimación Logit
    modelo_logit = smf.logit(formula, data=df).fit(cov_type='HC1')
    
    # Estimación Probit
    modelo_probit = smf.probit(formula, data=df).fit(cov_type='HC1')
    
    # Efectos marginales promedio (AME)
    ame_logit = modelo_logit.get_margeff(at='overall')
    ame_probit = modelo_probit.get_margeff(at='overall')
    
    return modelo_logit, modelo_probit, ame_logit, ame_probit

if __name__ == "__main__":
    print("Módulo de estimación econométrica listo.")
    