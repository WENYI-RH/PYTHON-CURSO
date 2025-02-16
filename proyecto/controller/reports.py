from config.app import *
import pandas as pd

def GenerateReportDescuentos (app: App):
    conn = app.bd.getConection()
    query = """
        SELECT 
            p.name AS producto,
            SUM(v.discount) AS total_descuento
        FROM 
            VENTAS v
        JOIN 
            PRODUCTOS p
        ON 
            v.product_id = p.id
        GROUP BY 
            p.name
        ORDER BY 
            total_descuento DESC;
    """
    df = pd.read_sql_query(query, conn)
    path = "/workspaces/PYTHON-CURSO/proyecto/files/data-descuentos.csv"
    df.to_csv(path)
    sendMail(app, path)

def sendMail(app: App, data):
    app.mail.send_email('from@example.com', 'Reporte de Descuentos', 'Reporte de Productos con Más Descuentos', data)
