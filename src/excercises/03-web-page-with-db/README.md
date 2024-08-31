# Static Webpage Deployment

## Use Case

In this exercise, we will reuse the last [webpage](../02-simple-web-page/README.md).

But we will add a couple of functionalities to transform this static webpage into a dynamic one.

The added features will be:
- Retrieve information about the existing characters in the Wheel of time
- The existing characters will be listed from the own DB
- The page will have a domain by DNS to have a more proper name

### Components

1. **Amazon S3**:
    - Serves as the storage for the static webpage files (HTML, CSS, JavaScript, images, etc.).
    - The bucket will be configured for static website hosting.
    - Permissions will be set to make the content publicly accessible.

2. **Lambda** + **API Gateway**:
    - Will be the bound between the webpage and the DynamoDB

3. **DynamoDB**:
    - All characters will be hosted in this NoSQL database 

4. **Route 53**:
   - Provides domain name system (DNS) service to map a custom domain to the CloudFront distribution.

### Steps

1. **Create an S3 Bucket**:
   - Name: `your-bucket-name`.
   - Enable static website hosting.
   - Upload the static webpage files (e.g., `index.html`, `styles.css`, `app.js`).
   - Set the appropriate permissions to allow public access to the files.

2. **Create the backend functionalities**:
   - Function to retrieve characters from the DB
   - Function to retrieve concrete attributes from an existing character

3. **Configure Route 53**:
   - Domain: If you have a custom domain, set up a hosted zone in Route 53.
   - Record Set: Create an A or CNAME record to point your domain to the CloudFront distribution.

### Accessing the Webpage

1. **Direct Access**:
   - URL: `http://your-bucket-name.s3-website-region.amazonaws.com`
   - Description: Users can access the static webpage directly via the S3 endpoint.

2. **Custom Domain (Optional)**:
   - URL: `https://www.yourdomain.com`
   - Description: If a custom domain is configured, users can access the static webpage via the user-friendly domain name.
