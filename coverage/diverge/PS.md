# PortSwigger

## Application Programming Interface

    Interface: a set of definitions and protocols, provides abstraction

    API: between two software components
    API endpoint: where an API receives requests about a specific resource
    API documentation: human-readable & machine-readable for ?automating task (e.g., API integration & validation)

    URI = scheme ":" ["//" authority] path ["?" query] ["#" fragment]

### >>> TestAPI

    Input (par) -- Type of requests -- Auth Mechanism
    
    Discovering API documentation
    Identifying API endpoints

    Identifying hidden params: 
    - Mass assignment (auto-binding): binding HTTP request params automatically into program code variables or objects

    Server-side param pollution:
    - Internal APIs that aren't directly accessible
      Embeds user input in a server-side request to

    - Query string: #, &, = 
        --URL-encode the--> %23, %26, ...
        --Interpret (at server-side)--> #, &, ...

        Truncating query strings
        Injecting (in)valid params
        Overriding existing params: same name 

    - RESTful API (similar to Path Travelsal, maybe...): may place param names and values in the URL path, rather than the query string

    - Structured data formats: manipulate params --exploit--> server's processing of other structured data formats
    

### >>> Tool

    Burp Scanner: crawl the API
    Burp Intruder: provide API's wordlist
    JS Link Finder: passively scanning JS files for endpoint links

    ?OpenAPI

### >>> Content-Type

    E.g.: JSON, XML
    Trigger errors, differences in processing logic

### >>> Method

    PATCH: partial changes to a resource
    OPTIONS: types of request methods permitted on a resource

### >>> PreventAPI

    Secure documentation 
    Use generic error messages

    Validate the content type & (an allowlist of) permitted HTTP methods

    Use protective measures on all versions
    
    Allowlist of characters don't need encoding
    Adheres to the expected format & structure 

## Path Traversal

### >>> TestPT

    Reading arbitrary files
    - ../ or /root
    - ....// or ..../\ if inner sequence is stripped
    - (Double) URL encoding: 
      ../ -> .%2e%2f -> .%2e%252f -> ..%c0%af -> ..%ef%bc%8f
    - ?Percent encoding
    - /Required-Base-Forder/../../...
    - .../filename%00.Expected-File-Extension

### >>> PreventPT

    Avoid

    Whitelist of permitted values or regex + Canonicalized path starts with the expected base directory.

## Business Logic

    Flawed assumptions about user behavior
    How different functions can be combined in unexpected ways

### >>> PreventBL

    Understand the domain
    Side-effects if the dependencies is malicious

    Avoid making implicit assumptions about user behavior or the behavior of other parts of the application

## SQL injection

    Interfere with the queries that an app makes to its DB

### >>> TestSQLi

    Retrieving hidden data
    Subverting application logic
    Second-order (stored)

    Retrieving data from other DB tables: UNION

    Blind: trigger conditionally a detectable DIFFERENCE 
    - DIFFERENCE: UI-based, Error-based, Time-based
    - With BinarySearch

    Examining the DB: type and version, contents
    - SELECT colname || ' ' || colname, NULL FROM tablename
    - ORDER BY colID

### >>> Detect

    Specific syntax (e.g. ', --) to the base value
    Condition (e.g. AND or OR), trigger time delays
    ? OAST payloads trigger an OOB network interaction (place the data into a DNS lookup for a domain that you control)

### >>> Mistake

    Oracle: SELECT NULL FROM dual :)))

## OS Command Injection
