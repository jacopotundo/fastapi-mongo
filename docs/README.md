# Documentazione Warehouse API

La documentazione è generata automaticamente usando **pdoc** con docstring in formato Google.

## Generare la documentazione

```bash
# Assicurati di essere nella root del progetto
cd c:\Users\A935apulia\Documents\GitHub\fastapi-mongo

# Attiva l'ambiente virtuale (se necessario)
factoryvenv\Scripts\activate

# Genera la documentazione
pdoc -o docs\pdoc --docformat google app
```

## Visualizzare la documentazione

Apri il file `docs\pdoc\app.html` nel browser.

## Struttura della documentazione

La documentazione include:

- **Core**: Configurazione e connessione al database
- **Models**: Modelli dati (Product, ProductStatus)
- **Schemas**: Schemi Pydantic per validazione API
- **Repositories**: Data access layer
- **Services**: Business logic
- **Routers**: Endpoint API

## Aggiornare la documentazione

Le docstring sono già state aggiunte a tutti i file. Se modifichi il codice, aggiorna anche le docstring e rigenera la documentazione con il comando sopra.
