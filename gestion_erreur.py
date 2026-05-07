import traceback
import linecache
from datetime import datetime

def gestion_erreur(erreur: TypeError, dossier_rapport: str = '.'):
    """
    Paramètres d'entrée:
        erreur: erreur à reporter
        dossier_rapport: dossier où enregistrer le rapport
    """
    rapport = f"Rapport d'erreur dans l'execution du programme\n\nDate : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    tb = erreur.__traceback__
    while tb.tb_next:
        tb = tb.tb_next
    error_frame = tb.tb_frame
    filename = error_frame.f_code.co_filename
    line_number = tb.tb_lineno

    rapport += f"Erreur dans le fichier : {filename} ligne : {line_number}\n\n"

    function_name = error_frame.f_code.co_name
    function_locals = error_frame.f_locals

    if function_name == "<module>":
        error_line = linecache.getline(filename, line_number).strip()
        rapport += f"Ligne ayant causée l'erreur : {error_line}\n"
        rapport += "Paramètres entrés :\n"
        for param, value in function_locals.items():
            if param in error_line:
                rapport += f"    - {param}: {value}\n"

    else:
    
        rapport += f"Fonction qui a causée l'erreur : {function_name}\n"
        rapport += "Paramètres entrés :\n"
        for param, value in function_locals.items():
            rapport += f"    - {param}: {value}\n"

    rapport += f"Message d'erreur : {str(e)}\n"

    with open(f'{dossier_rapport}/rapport_erreur_{datetime.now().strftime("%Y%m%d%H%M%S")}.txt', 'w') as f:
        f.write(rapport)
    return None

if __name__=='__main__':
    def fonction2(param):
        param = param+1

    def fonction3(param2):
        return param2 + "e"

    try:
        a = 1
        b = 0
        c = a/b
    except Exception as e:
        gestion_erreur(e, 'rapport')
