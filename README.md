# Hello World!

# Pipeline stages

running five stages: three for static code analysis, one for our  and ounit test and one for  deployment.

1. Code sanity

This is a code analyzer to enforce code style rules like the pep8 specification. 

2. complexity
This will detect the exitence of complexity.
This stage will throw an alert and fail if our code became too complex.


3. Code Security

Will detect any security issues such as
Use of assert
Hardcoded passwords
SQL injection
Binding to all interfaces
Weak cryptography
etc.


4. Unit Tests

5. Deployment
This is stage in will be simple staging deployment to Heroku


For a pull strategy, you can:
Have a cronjob that pulls your changes from Git and executes build.sh when it detects a new release.

