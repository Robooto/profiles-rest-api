
## Create custom user model
Gives you the ability over the user model fields

## See models on the admin site
* Register models in the admin.py file


## API Views

### APIView
Basic type of view - allows us to define functions for http methods
* Good for implementing complex logic
* Calling other apis
* Full contro lover logic
* Processing files and rendering a synchronous response

### ViewSets
Maps functions to operations - List, Create, Retrieve, Update, Partial Update, Destory
* Perfect for standard database operations
* Fastest way to make a database interface
* Good for simple CRUD interface for databases
    * when you don't need custom logic
    * have standard data structures

### ModelViewSet
Maps functions to operators for CRUD items

### Serializers
Converts json to python object

## Model Serializer
serialize a model to python object