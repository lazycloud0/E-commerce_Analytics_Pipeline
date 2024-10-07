from setuptools import setup, find_packages

# Define the package
setup(
    name='ecommerce_sales_analytics',   # Name of the package
    version='0.1.0',                    # Version of the package
    author='WL',                        # Author name
    author_email='',                    # Author email
    description='A data pipeline for e-commerce sales analytics',  # Short description
    packages=find_packages(),           # Automatically find packages in the project
    install_requires=[                  # List of dependencies
        'pandas==1.3.3',
        'sqlalchemy==1.4.22',
        'psycopg2-binary==2.9.1',
    ],
    classifiers=[                       # Optional classifiers
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',           # Minimum Python version required
)
