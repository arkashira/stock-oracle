# Tech Spec
## Stack
* Language: Python 3.10
* Framework: FastAPI 0.92.0
* Runtime: Uvicorn 0.20.0
* Database: PostgreSQL 14.5

## Hosting
* Platform: AWS
* Services:
	+ API Gateway: AWS API Gateway
	+ Compute: AWS Lambda
	+ Database: AWS RDS
	+ Storage: AWS S3
* Free-tier-first approach:
	+ Use AWS Free Tier for API Gateway, Lambda, and RDS

## Data Model
* Tables:
	+ **products**
		- id (primary key, integer)
		- sku (string)
		- name (string)
		- description (string)
	+ **inventory**
		- id (primary key, integer)
		- product_id (foreign key referencing products.id)
		- quantity (integer)
		- last_updated (timestamp)
	+ **fulfillment_centers**
		- id (primary key, integer)
		- name (string)
		- address (string)
	+ **vendors**
		- id (primary key, integer)
		- name (string)
		- address (string)
	+ **purchase_orders**
		- id (primary key, integer)
		- product_id (foreign key referencing products.id)
		- quantity (integer)
		- vendor_id (foreign key referencing vendors.id)
		- fulfillment_center_id (foreign key referencing fulfillment_centers.id)
		- status (string)
* Collections:
	+ **product_recommendations**
		- product_id (foreign key referencing products.id)
		- recommendation_score (float)

## API Surface
### Endpoints
1. **GET /products**: Retrieve a list of all products
	* Method: GET
	* Path: /products
	* Purpose: Retrieve a list of all products
2. **GET /products/{sku}**: Retrieve a product by SKU
	* Method: GET
	* Path: /products/{sku}
	* Purpose: Retrieve a product by SKU
3. **POST /purchase-orders**: Create a new purchase order
	* Method: POST
	* Path: /purchase-orders
	* Purpose: Create a new purchase order
4. **GET /purchase-orders**: Retrieve a list of all purchase orders
	* Method: GET
	* Path: /purchase-orders
	* Purpose: Retrieve a list of all purchase orders
5. **GET /fulfillment-centers**: Retrieve a list of all fulfillment centers
	* Method: GET
	* Path: /fulfillment-centers
	* Purpose: Retrieve a list of all fulfillment centers
6. **GET /vendors**: Retrieve a list of all vendors
	* Method: GET
	* Path: /vendors
	* Purpose: Retrieve a list of all vendors
7. **POST /inventory**: Update the inventory quantity of a product
	* Method: POST
	* Path: /inventory
	* Purpose: Update the inventory quantity of a product
8. **GET /product-recommendations**: Retrieve a list of product recommendations
	* Method: GET
	* Path: /product-recommendations
	* Purpose: Retrieve a list of product recommendations

## Security Model
* Authentication: JWT-based authentication using AWS Cognito
* Authorization: Role-based access control using AWS IAM
* Secrets management: AWS Secrets Manager
* Data encryption: SSL/TLS encryption for data in transit, AES-256 encryption for data at rest

## Observability
* Logging: AWS CloudWatch Logs
* Metrics: AWS CloudWatch Metrics
* Tracing: AWS X-Ray

## Build/CI
* Build tool: GitHub Actions
* CI pipeline:
	1. Build and package the application
	2. Run unit tests and integration tests
	3. Deploy the application to AWS
* Deployment strategy: Blue-green deployment using AWS CodeDeploy