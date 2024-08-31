# Static Webpage Deployment

## Use Case

In this exercise, you'll create and deploy a static webpage. The webpage will be hosted on Amazon S3. The webpage content will be written in HTML, CSS, and JavaScript.

### Overview

The application provides a simple static webpage that users can access through a web browser.

### Components

1. **Amazon S3**:
   - Serves as the storage for the static webpage files (HTML, CSS, JavaScript, images, etc.).
   - The bucket will be configured for static website hosting.
   - Permissions will be set to make the content publicly accessible.

### Steps

1. **Create an S3 Bucket**:
   - Name: `your-bucket-name`.
   - Enable static website hosting.
   - Upload the static webpage files (e.g., `index.html`, `error.html`).
   - Set the appropriate permissions to allow public access to the files.

### Accessing the Webpage

1. **Direct Access**:
   - URL: `http://your-bucket-name.s3-website-region.amazonaws.com`
   - Description: Users can access the static webpage directly via the S3 endpoint.

### Files Structure

- `index.html`: The main HTML file for the webpage.
- `error.html`: The error page when something goes wrong.
- `images/`: A directory containing image assets used on the webpage.

### Security Considerations

- Ensure the S3 bucket is configured to prevent public access to sensitive files.
