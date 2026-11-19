# questions.py
# Each row: (category, role, level, text, reference, keywords)
# category  : Technical | HR | Behavioral | Programming
# role      : Software Developer | Web Developer | Data Analyst | ML Engineer | Fresher (General)
# level     : Beginner | Intermediate | Advanced
# reference : a model answer used for similarity scoring
# keywords  : comma-separated important terms expected in a good answer
#
# Note: questions with role = "Fresher (General)" are treated as generic and are
# automatically included in the pool no matter which role the user selects
# (see the SQL query in app.py), so they add variety across every role.

QUESTIONS = [
    # ================= PROGRAMMING =================

    # -- Software Developer --
    ("Programming", "Software Developer", "Beginner",
     "What is the difference between a compiler and an interpreter?",
     "A compiler translates the entire source code into machine code before execution, "
     "producing an executable file, while an interpreter translates and executes code "
     "line by line without producing a separate executable.",
     "compiler,interpreter,machine code,translate,execute,line by line"),

    ("Programming", "Software Developer", "Beginner",
     "What is inheritance in object oriented programming?",
     "Inheritance is an OOP concept where a class, called the child or subclass, "
     "acquires the properties and methods of another class, called the parent or "
     "superclass, allowing code reuse and hierarchical relationships.",
     "inheritance,class,subclass,parent class,reuse,oop"),

    ("Programming", "Software Developer", "Beginner",
     "What is the difference between a function and a method?",
     "A function is an independent, reusable block of code that can be called on "
     "its own, while a method is a function that is defined inside a class and "
     "operates on an object of that class.",
     "function,method,class,object,reusable,independent"),
    
    ("Programming", "Software Developer", "Beginner",
     "What is encapsulation in object-oriented programming?",
     "Encapsulation is an object-oriented programming concept that combines data and the methods that operate on it inside a class. It restricts direct access to some internal details and allows controlled access through methods such as getters and setters.",
     "encapsulation,oop,class,data hiding,getter,setter,access"),

    ("Programming", "Software Developer", "Beginner",
     "What is the difference between a local variable and a global variable?",
     "A local variable is declared inside a function or block and can generally be accessed only within that scope, while a global variable is declared outside functions and can be accessed from multiple parts of a program according to the language's scope rules.",
     "local variable,global variable,scope,function,block,access"),

    ("Programming", "Software Developer", "Beginner",
     "What is an exception in programming?",
     "An exception is an event that occurs during program execution and interrupts the normal flow of instructions. Exception handling constructs such as try, catch or except allow a program to respond to errors gracefully.",
     "exception,error,runtime,try,catch,except,exception handling"),



    ("Programming", "Software Developer", "Beginner",
     "What is a variable and why do we use data types?",
     "A variable is a named location in memory used to store a value, and data "
     "types tell the compiler or interpreter what kind of value is stored, such "
     "as integer, string or boolean, so operations on it are valid and memory is "
     "allocated correctly.",
     "variable,memory,data type,integer,string,boolean,allocation"),

    ("Programming", "Software Developer", "Intermediate",
     "Explain the difference between an array and a linked list.",
     "An array stores elements in contiguous memory with constant time random access "
     "but costly insertion or deletion, while a linked list stores elements as nodes "
     "connected by pointers, allowing efficient insertion and deletion but only "
     "sequential access.",
     "array,linked list,contiguous memory,pointer,insertion,deletion,random access"),

    ("Programming", "Software Developer", "Intermediate",
     "What is the time complexity of binary search and why?",
     "Binary search runs in O(log n) time because it repeatedly divides the sorted "
     "search space in half, discarding one half at every comparison until the target "
     "element is found or the space is empty.",
     "binary search,log n,sorted,divide,half,time complexity"),

    ("Programming", "Software Developer", "Intermediate",
     "What is the difference between stack and queue data structures?",
     "A stack follows Last In First Out order where elements are added and removed "
     "from the same end, while a queue follows First In First Out order where "
     "elements are added at the rear and removed from the front.",
     "stack,queue,lifo,fifo,push,pop,enqueue,dequeue"),

    ("Programming", "Software Developer", "Intermediate",
     "What is recursion and what are its risks?",
     "Recursion is when a function calls itself to solve smaller instances of a "
     "problem until it reaches a base case; if the base case is missing or "
     "incorrect it can cause infinite recursion and a stack overflow.",
     "recursion,base case,function calls itself,stack overflow,infinite"),

    ("Programming", "Software Developer", "Advanced",
     "How does a hash map achieve average O(1) time complexity for lookups?",
     "A hash map applies a hash function to a key to compute an index into an array "
     "of buckets, so lookup, insertion and deletion take average constant time, "
     "though collisions handled through chaining or open addressing can degrade "
     "performance in the worst case.",
     "hash function,bucket,index,collision,chaining,constant time,worst case"),

    ("Programming", "Software Developer", "Intermediate",
     "What is polymorphism in object-oriented programming?",
     "Polymorphism means that the same interface or method name can represent different behaviors depending on the object or data type. It supports flexibility and allows different classes to provide their own implementations of a common method.",
     "polymorphism,oop,method overriding,overloading,interface,flexibility"),

    ("Programming", "Software Developer", "Intermediate",
     "What is the difference between an abstract class and an interface?",
     "An abstract class can provide both implemented methods and abstract methods, and it can maintain instance state. An interface primarily defines a contract that implementing classes must follow; the exact features supported by interfaces depend on the programming language.",
     "abstract class,interface,abstract method,implementation,contract,class"),

    ("Programming", "Software Developer", "Intermediate",
     "What is a constructor and when is it called?",
     "A constructor is a special class member used to initialize a newly created object. It is generally called automatically when an object is instantiated, and it can assign initial values to the object's fields.",
     "constructor,object,initialize,instantiate,class,fields"),

    ("Programming", "Software Developer", "Intermediate",
     "What is the difference between pass by value and pass by reference?",
     "In pass by value, a function receives a copy of an argument's value, so changing the parameter does not directly change the caller's variable. In pass by reference, the function can access the original variable through a reference and may modify it; exact behavior depends on the language.",
     "pass by value,pass by reference,argument,parameter,copy,reference"),


    ("Programming", "Software Developer", "Advanced",
     "What is the difference between multithreading and multiprocessing?",
     "Multithreading runs multiple threads within a single process sharing the "
     "same memory space, which is lightweight but risks race conditions, while "
     "multiprocessing runs multiple independent processes each with its own "
     "memory space, offering better isolation at higher resource cost.",
     "multithreading,multiprocessing,thread,process,memory space,race condition"),
    
    ("Programming", "Software Developer", "Advanced",
     "What is a race condition in concurrent programming?",
     "A race condition occurs when multiple threads or processes access shared data concurrently and the final result depends on the unpredictable order of execution. It can be prevented or controlled using synchronization mechanisms such as locks, mutexes and atomic operations.",
     "race condition,concurrency,shared data,thread,process,lock,mutex,synchronization"),



    # -- Web Developer --
    ("Programming", "Web Developer", "Beginner",
     "What is the difference between HTML and CSS?",
     "HTML defines the structure and content of a web page using elements and tags, "
     "while CSS is used to style that content, controlling layout, colors, fonts "
     "and responsiveness.",
     "html,css,structure,content,style,layout"),

    ("Programming", "Web Developer", "Beginner",
     "What is the DOM in web development?",
     "The DOM, or Document Object Model, is a tree-like representation of an HTML "
     "page in memory that browsers create, allowing JavaScript to read and "
     "dynamically change the content, structure and style of the page.",
     "dom,document object model,tree,javascript,html page,dynamic"),

    ("Programming", "Web Developer", "Beginner",
     "What is the difference between frontend and backend development?",
     "Frontend development focuses on the part of a website that users see and interact with, including layout and user interface. Backend development handles server-side logic, data processing, authentication and communication with databases.",
     "frontend,backend,user interface,server,database,logic"),

    ("Programming", "Web Developer", "Beginner",
     "What is the purpose of JavaScript in web development?",
     "JavaScript adds behavior and interactivity to web pages. It can respond to user events, validate forms, update page content dynamically and communicate with servers without requiring a full page reload.",
     "javascript,interactivity,event,dynamic content,form validation,web page"),


    ("Programming", "Web Developer", "Intermediate",
     "What is the difference between GET and POST HTTP methods?",
     "GET requests retrieve data and append parameters to the URL, are cacheable "
     "and should not change server state, while POST requests send data in the "
     "request body, are typically used to create or update resources, and are not "
     "cached by default.",
     "get,post,http method,url,request body,idempotent,cache"),

    ("Programming", "Web Developer", "Intermediate",
     "What is responsive web design and how is it achieved?",
     "Responsive web design makes a website adapt its layout to different screen "
     "sizes and devices, typically achieved using flexible grids, relative units, "
     "media queries and frameworks like Bootstrap.",
     "responsive,media query,flexible grid,screen size,bootstrap,layout"),

    ("Programming", "Web Developer", "Advanced",
     "How does the browser's event loop handle asynchronous JavaScript code?",
     "JavaScript is single threaded and uses an event loop that moves completed "
     "callbacks from the task queue and microtask queue onto the call stack once "
     "it is empty, allowing asynchronous operations like promises and timers to "
     "run without blocking the main thread.",
     "event loop,call stack,callback,queue,asynchronous,promise,single threaded"),

    ("Programming", "Web Developer", "Advanced",
     "What is Cross-Site Scripting (XSS) and how can it be prevented?",
     "Cross-Site Scripting is a vulnerability where an attacker injects malicious "
     "scripts into a web page viewed by other users; it can be prevented by "
     "sanitizing and escaping user input, using content security policies, and "
     "avoiding directly inserting untrusted input into the DOM.",
     "xss,cross site scripting,injection,sanitize,escape,security,user input"),

    
    ("Programming", "Web Developer", "Advanced",
     "What is CORS and why is it required?",
     "Cross-Origin Resource Sharing is a browser security mechanism that uses HTTP headers to specify whether a web page from one origin may access resources from another origin. It allows servers to grant controlled cross-origin access.",
     "cors,cross-origin,browser,security,http headers,origin,access"),


    # -- Fresher (General) / Programming --
    ("Programming", "Fresher (General)", "Beginner",
     "What is a loop and why is it used in programming?",
     "A loop is a control structure that repeats a block of code as long as a "
     "condition is true, and it is used to avoid writing repetitive code for "
     "tasks such as iterating over a list or repeating an action multiple times.",
     "loop,repeat,condition,iterate,control structure"),

    ("Programming", "Fresher (General)", "Beginner",
     "What is the difference between a list and a tuple in Python?",
     "A list is mutable, meaning its elements can be changed after creation, "
     "while a tuple is immutable, meaning once created its elements cannot be "
     "modified; both can store an ordered collection of items.",
     "list,tuple,mutable,immutable,python,ordered collection"),

     ("Programming", "Fresher (General)", "Beginner",
     "What is the difference between a syntax error and a logical error?",
     "A syntax error occurs when code violates the grammar rules of a programming language and may prevent the program from running. A logical error occurs when the program runs but produces an incorrect result because its logic is wrong.",
     "syntax error,logical error,grammar,program execution,incorrect result,debugging"),

    ("Programming", "Fresher (General)", "Beginner",
     "What is an algorithm?",
     "An algorithm is a finite sequence of clear and ordered steps used to solve a problem or perform a task. A good algorithm should produce the required result and should eventually terminate.",
     "algorithm,steps,problem solving,finite,ordered,terminate"),


    ("Programming", "Fresher (General)", "Intermediate",
     "What is an API and why is it useful?",
     "An API, or Application Programming Interface, is a set of rules that "
     "allows different software applications to communicate with each other, "
     "letting a developer use functionality from another service without "
     "knowing its internal implementation.",
     "api,application programming interface,communicate,functionality,request"),

    ("Programming", "Fresher (General)", "Intermediate",
     "What is version control and why is Git commonly used?",
     "Version control is a system that tracks changes to source code over time, "
     "allowing multiple developers to collaborate, revert to earlier versions, "
     "and manage different branches of development; Git is widely used because "
     "it is distributed, fast and supports branching and merging.",
     "version control,git,track changes,branch,merge,collaborate"),

    # ================= TECHNICAL =================

    # -- Data Analyst --
    ("Technical", "Data Analyst", "Beginner",
     "What is the difference between a primary key and a foreign key?",
     "A primary key uniquely identifies each record in a table and cannot be null, "
     "while a foreign key is a field in one table that references the primary key "
     "of another table to establish a relationship between the two tables.",
     "primary key,foreign key,unique,relationship,table,reference"),

    ("Technical", "Data Analyst", "Beginner",
     "What is the difference between structured and unstructured data?",
     "Structured data is organized in a fixed format such as rows and columns in "
     "a database, making it easy to search and analyze, while unstructured data "
     "such as images, videos or free text has no predefined format.",
     "structured data,unstructured data,rows,columns,database,format"),

    ("Technical", "Data Analyst", "Intermediate",
     "What is the difference between INNER JOIN and LEFT JOIN in SQL?",
     "An INNER JOIN returns only the rows that have matching values in both tables, "
     "while a LEFT JOIN returns all rows from the left table along with matching "
     "rows from the right table, filling unmatched columns with null.",
     "inner join,left join,matching rows,null,sql,table"),

    ("Technical", "Data Analyst", "Intermediate",
     "What is data normalization and why is it used?",
     "Data normalization is the process of organizing database tables to reduce "
     "redundancy and improve data integrity by dividing large tables into smaller, "
     "related tables and defining relationships between them.",
     "normalization,redundancy,data integrity,tables,relationships"),

    ("Technical", "Data Analyst", "Intermediate",
     "What is the difference between GROUP BY and ORDER BY in SQL?",
     "GROUP BY groups rows that share the same values in specified columns so "
     "aggregate functions like COUNT or SUM can be applied to each group, while "
     "ORDER BY simply sorts the result set based on one or more columns.",
     "group by,order by,aggregate,sum,count,sort,sql"),

    ("Technical", "Data Analyst", "Advanced",
     "How would you handle missing values in a dataset before analysis?",
     "Missing values can be handled by removing rows or columns with excessive "
     "missing data, imputing values using the mean, median or mode, or using "
     "predictive models to estimate missing values, depending on the amount and "
     "pattern of missingness.",
     "missing values,imputation,mean,median,mode,remove,dataset"),

    ("Technical", "Data Analyst", "Advanced",
     "What is the difference between a data warehouse and a database?",
     "A database is designed for day to day transactional operations with "
     "frequent reads and writes, while a data warehouse is designed for large "
     "scale analytical queries and reporting, consolidating historical data "
     "from multiple sources for business intelligence.",
     "data warehouse,database,transactional,analytical,reporting,historical data"),

    # -- ML Engineer --
    ("Technical", "ML Engineer", "Beginner",
     "What is the difference between supervised and unsupervised learning?",
     "Supervised learning trains a model on labeled data where the correct output "
     "is known, while unsupervised learning finds patterns or groupings in "
     "unlabeled data without predefined output labels.",
     "supervised,unsupervised,labeled data,pattern,model"),

    ("Technical", "ML Engineer", "Beginner",
     "What is the difference between classification and regression?",
     "Classification predicts a discrete category or class label, such as spam "
     "or not spam, while regression predicts a continuous numeric value, such as "
     "predicting a house price.",
     "classification,regression,discrete,continuous,category,numeric value"),

    ("Technical", "ML Engineer", "Intermediate",
     "What is overfitting and how can it be reduced?",
     "Overfitting occurs when a model learns the training data too closely, "
     "including noise, and performs poorly on new data; it can be reduced using "
     "techniques such as cross validation, regularization, pruning, or gathering "
     "more training data.",
     "overfitting,training data,regularization,cross validation,generalization"),

    ("Technical", "ML Engineer", "Intermediate",
     "What is a confusion matrix used for?",
     "A confusion matrix is a table used to evaluate a classification model by "
     "showing counts of true positives, true negatives, false positives and "
     "false negatives, helping calculate metrics like accuracy, precision and "
     "recall.",
     "confusion matrix,true positive,false positive,accuracy,precision,recall"),

    ("Technical", "ML Engineer", "Advanced",
     "Explain how cosine similarity is used to compare two text documents.",
     "Cosine similarity represents each document as a vector, for example using "
     "TF-IDF weights, and measures the cosine of the angle between the two "
     "vectors; a value close to one indicates high similarity in content while a "
     "value close to zero indicates the documents are unrelated.",
     "cosine similarity,vector,tf-idf,angle,similarity score,document"),

    ("Technical", "ML Engineer", "Advanced",
     "What is the bias-variance tradeoff in machine learning?",
     "The bias-variance tradeoff describes the balance between a model's error "
     "from overly simplistic assumptions, called bias, and its error from being "
     "too sensitive to fluctuations in the training data, called variance; "
     "reducing one often increases the other, so the goal is to find a good "
     "balance for generalization.",
     "bias,variance,tradeoff,generalization,overfitting,underfitting"),

    # -- Fresher (General) / Technical --
    ("Technical", "Fresher (General)", "Beginner",
     "What is the difference between RAM and ROM?",
     "RAM, or Random Access Memory, is volatile memory used to temporarily "
     "store data that the processor is actively using, while ROM, or Read Only "
     "Memory, is non-volatile memory that permanently stores instructions such "
     "as those needed to start a computer.",
     "ram,rom,volatile,non-volatile,memory,processor"),

    ("Technical", "Fresher (General)", "Beginner",
     "What is the difference between a process and a thread?",
     "A process is an independent program in execution with its own memory "
     "space, while a thread is a smaller unit of execution within a process "
     "that shares the same memory space with other threads of that process.",
     "process,thread,memory space,execution,independent,shared"),

    ("Technical", "Fresher (General)", "Intermediate",
     "What is the difference between HTTP and HTTPS?",
     "HTTP is a protocol used to transfer data between a browser and a server "
     "in plain text, while HTTPS adds a layer of encryption using SSL or TLS, "
     "making the communication secure and protecting data from eavesdropping.",
     "http,https,protocol,encryption,ssl,tls,secure"),

    ("Technical", "Fresher (General)", "Intermediate",
     "What is an operating system and what are its main functions?",
     "An operating system is software that manages computer hardware and "
     "software resources, providing services such as process management, "
     "memory management, file system management and handling input and output "
     "devices.",
     "operating system,process management,memory management,file system,hardware"),

    # ================= HR =================

    ("HR", "Fresher (General)", "Beginner",
     "Tell me about yourself.",
     "A good answer briefly introduces educational background, key skills, "
     "relevant projects or experience, and ends with career goals relevant to "
     "the role being applied for.",
     "background,skills,education,projects,goals,experience"),

    ("HR", "Fresher (General)", "Beginner",
     "Why do you want to work for this company?",
     "A strong answer shows the candidate has researched the company, connects "
     "the company's work or values with their own skills and interests, and "
     "explains how they can contribute to the company's goals.",
     "company,research,values,contribute,skills,goals"),

    ("HR", "Fresher (General)", "Beginner",
     "What do you know about this role?",
     "A good answer shows the candidate has read the job description carefully, "
     "understands the key responsibilities and required skills, and can explain "
     "how their own background fits those requirements.",
     "job description,responsibilities,skills,role,fit"),

    ("HR", "Fresher (General)", "Intermediate",
     "Where do you see yourself in five years?",
     "A good answer shows realistic career growth aligned with the company or "
     "industry, expresses willingness to learn new skills, and shows ambition "
     "balanced with commitment to the role.",
     "career growth,five years,learning,ambition,goals"),

    ("HR", "Fresher (General)", "Intermediate",
     "What are your strengths and weaknesses?",
     "A good answer names genuine strengths relevant to the job with examples, "
     "and mentions a real weakness along with the steps being taken to improve "
     "it, showing self awareness.",
     "strengths,weaknesses,examples,self awareness,improvement"),

    ("HR", "Fresher (General)", "Intermediate",
     "How do you handle stress and pressure at work?",
     "A good answer describes specific strategies such as prioritizing tasks, "
     "breaking work into smaller steps, staying organized, and remaining calm, "
     "ideally supported with a real example of handling a pressured situation.",
     "stress,pressure,prioritize,organized,example,calm"),

    ("HR", "Fresher (General)", "Advanced",
     "Why should we hire you?",
     "A strong answer connects the candidate's specific skills, projects, and "
     "achievements directly to the requirements of the job, explaining what "
     "unique value they bring compared to other candidates.",
     "skills,achievements,job requirements,unique value,fit"),

    ("HR", "Fresher (General)", "Advanced",
     "What are your salary expectations?",
     "A good answer shows the candidate has researched typical industry and "
     "role-based compensation, states a realistic and flexible range, and "
     "frames the answer around the value they can bring rather than a fixed "
     "demand.",
     "salary,expectations,research,range,flexible,value"),

    # ================= BEHAVIORAL =================

    ("Behavioral", "Fresher (General)", "Beginner",
     "Describe a situation where you worked as part of a team.",
     "A good STAR-style answer describes the Situation and Task, the Action the "
     "candidate personally took as part of the team, and the positive Result "
     "achieved, highlighting collaboration and communication.",
     "situation,task,action,result,team,collaboration,communication"),

    ("Behavioral", "Fresher (General)", "Beginner",
     "Describe a time you had to learn something new quickly.",
     "A good STAR-style answer describes the situation requiring fast learning, "
     "the specific steps taken to learn the new skill or concept, and the "
     "positive outcome, showing adaptability and initiative.",
     "situation,learn,action,result,adaptability,initiative"),

    ("Behavioral", "Fresher (General)", "Intermediate",
     "Tell me about a time you faced a difficult problem and how you solved it.",
     "A good STAR-style answer explains the specific problem faced, the "
     "reasoning or steps taken to analyze and solve it, and the outcome, "
     "showing problem solving skills and persistence.",
     "situation,problem,action,solution,result,persistence,problem solving"),

    ("Behavioral", "Fresher (General)", "Intermediate",
     "Describe a time you had a disagreement with a teammate and how you handled it.",
     "A good STAR-style answer describes the disagreement calmly, focuses on "
     "the actions taken to communicate and reach a resolution, and highlights "
     "a positive outcome and lesson learned.",
     "situation,disagreement,communication,resolution,result,teamwork"),

    ("Behavioral", "Fresher (General)", "Intermediate",
     "Tell me about a time you had to manage multiple deadlines at once.",
     "A good STAR-style answer describes the competing deadlines, the specific "
     "prioritization or time management approach used, and the successful "
     "result, showing organization and time management skills.",
     "situation,deadlines,prioritize,time management,action,result"),

    ("Behavioral", "Fresher (General)", "Advanced",
     "Tell me about a time you failed at something and what you learned from it.",
     "A good STAR-style answer honestly describes the situation and failure, "
     "focuses on the specific actions taken afterward, and clearly explains the "
     "lesson learned and how it changed future behavior.",
     "situation,failure,action,lesson,result,growth,improvement"),

    ("Behavioral", "Fresher (General)", "Advanced",
     "Describe a time you took initiative without being asked.",
     "A good STAR-style answer describes the situation where no one assigned "
     "the task, the specific action taken on the candidate's own initiative, "
     "and the positive result, showing proactiveness and ownership.",
     "situation,initiative,action,proactive,ownership,result"),
]
