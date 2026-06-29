"""
Realistic synthetic candidate seed data — 20 candidates across different roles and seniority levels.
Swap this out with your real candidates.jsonl or sample_candidates.json when ready.
"""

SEED_CANDIDATES = [
    {
        "candidate_id": "C001",
        "name": "Arjun Mehta",
        "headline": "Senior ML Engineer | NLP & LLM Specialist",
        "summary": "Passionate ML engineer with 7 years building production NLP systems. Led teams at two AI startups. Strong open-source contributor.",
        "skills": ["Python", "PyTorch", "NLP", "LLMs", "HuggingFace", "FastAPI", "Docker", "Kubernetes", "MLflow"],
        "total_experience_years": 7.0,
        "work_history": [
            {"company": "Sarvam AI", "title": "Senior ML Engineer", "duration_months": 24, "description": "Built multilingual LLM pipelines for Indian languages. Led team of 5."},
            {"company": "Bangalore ML Labs", "title": "ML Engineer", "duration_months": 36, "description": "Developed NLP models for document classification and extraction."}
        ],
        "education": [{"degree": "M.Tech", "field": "AI & Machine Learning", "institution": "IIT Bombay"}],
        "activity": {"github_active": True, "open_source_contributions": 45, "blog_posts": 12, "last_active_days_ago": 3, "certifications_recent": 2},
        "location": "Bangalore, India",
        "expected_role_level": "senior"
    },
    {
        "candidate_id": "C002",
        "name": "Priya Venkataraman",
        "headline": "Data Scientist | Recommendation Systems & Analytics",
        "summary": "Data scientist specializing in recommendation engines and A/B testing. 5 years experience at product companies.",
        "skills": ["Python", "Scikit-learn", "TensorFlow", "SQL", "Spark", "Airflow", "Statistics", "A/B Testing", "Tableau"],
        "total_experience_years": 5.0,
        "work_history": [
            {"company": "Flipkart", "title": "Data Scientist II", "duration_months": 30, "description": "Built recommendation system serving 100M+ users."},
            {"company": "Mu Sigma", "title": "Data Analyst", "duration_months": 18, "description": "Delivered analytics dashboards for FMCG clients."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "NIT Trichy"}],
        "activity": {"github_active": True, "open_source_contributions": 12, "blog_posts": 5, "last_active_days_ago": 14, "certifications_recent": 1},
        "location": "Chennai, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C003",
        "name": "Rohan Das",
        "headline": "Full Stack Engineer | React & Node.js Expert",
        "summary": "Full-stack engineer with 4 years building scalable SaaS products. Passionate about clean code and great UX.",
        "skills": ["React", "Node.js", "TypeScript", "PostgreSQL", "Redis", "AWS", "Docker", "GraphQL", "REST APIs"],
        "total_experience_years": 4.0,
        "work_history": [
            {"company": "Razorpay", "title": "Software Engineer II", "duration_months": 28, "description": "Built payment dashboard used by 500K merchants."},
            {"company": "Freshworks", "title": "Frontend Developer", "duration_months": 18, "description": "Developed CRM features with React and TypeScript."}
        ],
        "education": [{"degree": "B.E.", "field": "Computer Science", "institution": "VIT Vellore"}],
        "activity": {"github_active": True, "open_source_contributions": 8, "blog_posts": 3, "last_active_days_ago": 7, "certifications_recent": 1},
        "location": "Hyderabad, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C004",
        "name": "Sneha Iyer",
        "headline": "AI Research Engineer | Computer Vision",
        "summary": "Research engineer focused on computer vision and real-time inference. Published 3 papers. Ex-DRDO researcher.",
        "skills": ["Python", "PyTorch", "OpenCV", "YOLO", "TensorRT", "CUDA", "C++", "Docker", "MLflow"],
        "total_experience_years": 6.0,
        "work_history": [
            {"company": "Mad Street Den (Vue.ai)", "title": "AI Research Engineer", "duration_months": 30, "description": "Built visual search and fashion tagging models."},
            {"company": "DRDO", "title": "Research Fellow", "duration_months": 24, "description": "Computer vision for defence applications."}
        ],
        "education": [{"degree": "M.S.", "field": "Computer Science", "institution": "IISc Bangalore"}],
        "activity": {"github_active": True, "open_source_contributions": 20, "blog_posts": 8, "last_active_days_ago": 21, "certifications_recent": 0},
        "location": "Bangalore, India",
        "expected_role_level": "senior"
    },
    {
        "candidate_id": "C005",
        "name": "Karan Sharma",
        "headline": "Backend Engineer | Java & Microservices",
        "summary": "Backend engineer with 8 years building high-throughput microservices. Loves distributed systems and performance tuning.",
        "skills": ["Java", "Spring Boot", "Kafka", "PostgreSQL", "Redis", "AWS", "Docker", "Kubernetes", "Microservices"],
        "total_experience_years": 8.0,
        "work_history": [
            {"company": "PhonePe", "title": "Senior Backend Engineer", "duration_months": 36, "description": "Built payment processing microservices handling 10M TPS."},
            {"company": "Infosys", "title": "Associate Consultant", "duration_months": 36, "description": "Java microservices for banking clients."}
        ],
        "education": [{"degree": "B.Tech", "field": "Information Technology", "institution": "BITS Pilani"}],
        "activity": {"github_active": False, "open_source_contributions": 2, "blog_posts": 1, "last_active_days_ago": 90, "certifications_recent": 1},
        "location": "Pune, India",
        "expected_role_level": "senior"
    },
    {
        "candidate_id": "C006",
        "name": "Divya Nair",
        "headline": "DevOps & Cloud Engineer | AWS Certified",
        "summary": "DevOps engineer with 5 years automating infrastructure and building CI/CD pipelines. AWS and GCP certified.",
        "skills": ["AWS", "GCP", "Terraform", "Kubernetes", "Docker", "Jenkins", "Ansible", "Python", "Bash", "Prometheus"],
        "total_experience_years": 5.0,
        "work_history": [
            {"company": "Walmart Global Tech", "title": "DevOps Engineer II", "duration_months": 30, "description": "Managed cloud infra for Indian e-commerce operations."},
            {"company": "TCS", "title": "Cloud Engineer", "duration_months": 24, "description": "Migrated legacy apps to AWS for retail clients."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "SRM University"}],
        "activity": {"github_active": True, "open_source_contributions": 6, "blog_posts": 4, "last_active_days_ago": 10, "certifications_recent": 3},
        "location": "Chennai, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C007",
        "name": "Amit Patel",
        "headline": "Data Engineer | Spark & Big Data Pipelines",
        "summary": "Data engineer building large-scale ETL pipelines and lakehouses. 6 years experience in fintech and e-commerce.",
        "skills": ["Python", "Spark", "Airflow", "dbt", "Snowflake", "Kafka", "SQL", "AWS Glue", "Delta Lake"],
        "total_experience_years": 6.0,
        "work_history": [
            {"company": "Zepto", "title": "Senior Data Engineer", "duration_months": 18, "description": "Built real-time data pipelines for quick commerce analytics."},
            {"company": "HDFC Bank Tech", "title": "Data Engineer", "duration_months": 42, "description": "Designed fraud detection data infrastructure."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "NIT Surathkal"}],
        "activity": {"github_active": True, "open_source_contributions": 9, "blog_posts": 2, "last_active_days_ago": 30, "certifications_recent": 2},
        "location": "Mumbai, India",
        "expected_role_level": "senior"
    },
    {
        "candidate_id": "C008",
        "name": "Lakshmi Reddy",
        "headline": "Product Manager | AI & Consumer Tech",
        "summary": "PM with 4 years driving AI product strategy at consumer tech companies. Strong data-driven decision maker.",
        "skills": ["Product Strategy", "Data Analysis", "SQL", "A/B Testing", "Roadmapping", "User Research", "Figma", "JIRA", "Python"],
        "total_experience_years": 4.0,
        "work_history": [
            {"company": "Meesho", "title": "Product Manager", "duration_months": 24, "description": "Launched AI-powered seller tools increasing GMV by 30%."},
            {"company": "OYO", "title": "Associate PM", "duration_months": 18, "description": "Managed booking and pricing features."}
        ],
        "education": [{"degree": "MBA", "field": "Marketing & Strategy", "institution": "IIM Kozhikode"}],
        "activity": {"github_active": False, "open_source_contributions": 0, "blog_posts": 7, "last_active_days_ago": 15, "certifications_recent": 1},
        "location": "Bangalore, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C009",
        "name": "Vikas Gupta",
        "headline": "Junior Python Developer | Django & REST APIs",
        "summary": "Junior developer with 1.5 years building REST APIs with Django. Eager learner, actively building side projects.",
        "skills": ["Python", "Django", "REST APIs", "PostgreSQL", "Git", "HTML", "CSS", "JavaScript"],
        "total_experience_years": 1.5,
        "work_history": [
            {"company": "Sigmoid Analytics", "title": "Junior Software Engineer", "duration_months": 18, "description": "Built internal REST APIs for analytics platform."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "Amity University"}],
        "activity": {"github_active": True, "open_source_contributions": 3, "blog_posts": 1, "last_active_days_ago": 5, "certifications_recent": 2},
        "location": "Delhi, India",
        "expected_role_level": "junior"
    },
    {
        "candidate_id": "C010",
        "name": "Meera Krishnan",
        "headline": "NLP Engineer | Conversational AI & Chatbots",
        "summary": "NLP engineer building conversational AI systems for 4 years. Expert in BERT fine-tuning and dialogue systems.",
        "skills": ["Python", "NLP", "BERT", "Transformers", "Rasa", "FastAPI", "HuggingFace", "LangChain", "Pinecone"],
        "total_experience_years": 4.0,
        "work_history": [
            {"company": "Yellow.ai", "title": "NLP Engineer", "duration_months": 30, "description": "Built enterprise chatbots in 10+ languages."},
            {"company": "Wipro", "title": "Software Engineer", "duration_months": 18, "description": "NLP models for document processing."}
        ],
        "education": [{"degree": "M.Tech", "field": "Computational Linguistics", "institution": "IIT Madras"}],
        "activity": {"github_active": True, "open_source_contributions": 18, "blog_posts": 9, "last_active_days_ago": 8, "certifications_recent": 1},
        "location": "Hyderabad, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C011",
        "name": "Rahul Joshi",
        "headline": "Lead Data Scientist | Head of AI at EdTech",
        "summary": "Lead data scientist with 10 years experience. Built and managed AI teams. Expert in ML strategy and deployment.",
        "skills": ["Python", "ML Strategy", "TensorFlow", "Spark", "Leadership", "MLOps", "Statistics", "SQL", "Tableau"],
        "total_experience_years": 10.0,
        "work_history": [
            {"company": "BYJU's", "title": "Head of Data Science", "duration_months": 36, "description": "Led 15-person AI team building personalized learning engine."},
            {"company": "Paytm", "title": "Senior Data Scientist", "duration_months": 36, "description": "Built credit scoring and fraud models."}
        ],
        "education": [{"degree": "M.Tech", "field": "Statistics & Computing", "institution": "IIT Delhi"}],
        "activity": {"github_active": False, "open_source_contributions": 3, "blog_posts": 15, "last_active_days_ago": 45, "certifications_recent": 0},
        "location": "Mumbai, India",
        "expected_role_level": "lead"
    },
    {
        "candidate_id": "C012",
        "name": "Ananya Singh",
        "headline": "Frontend Developer | Vue.js & UX Engineering",
        "summary": "Frontend engineer with 3 years crafting pixel-perfect UIs. Specializes in Vue.js, animations, and accessibility.",
        "skills": ["Vue.js", "JavaScript", "TypeScript", "CSS", "Figma", "Webpack", "Jest", "REST APIs", "WCAG"],
        "total_experience_years": 3.0,
        "work_history": [
            {"company": "InMobi", "title": "Frontend Engineer", "duration_months": 24, "description": "Built ad analytics dashboard with complex data visualizations."},
            {"company": "Capgemini", "title": "Junior Frontend Developer", "duration_months": 12, "description": "Vue.js components for enterprise portal."}
        ],
        "education": [{"degree": "B.E.", "field": "Information Science", "institution": "BMS College of Engineering"}],
        "activity": {"github_active": True, "open_source_contributions": 5, "blog_posts": 6, "last_active_days_ago": 12, "certifications_recent": 1},
        "location": "Bangalore, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C013",
        "name": "Siddharth Rao",
        "headline": "MLOps Engineer | Model Deployment & Monitoring",
        "summary": "MLOps engineer bridging ML and DevOps. Builds model serving infra, drift monitoring, and retraining pipelines.",
        "skills": ["Python", "MLflow", "Kubeflow", "Docker", "Kubernetes", "Prometheus", "FastAPI", "AWS SageMaker", "DVC"],
        "total_experience_years": 5.0,
        "work_history": [
            {"company": "Lenskart", "title": "MLOps Engineer", "duration_months": 24, "description": "Deployed 20+ models to production. Built A/B testing framework."},
            {"company": "Accenture AI", "title": "ML Engineer", "duration_months": 36, "description": "Model deployment pipelines for banking clients."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "DTU Delhi"}],
        "activity": {"github_active": True, "open_source_contributions": 14, "blog_posts": 4, "last_active_days_ago": 6, "certifications_recent": 3},
        "location": "Delhi, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C014",
        "name": "Neha Bansal",
        "headline": "Android Developer | Kotlin & Jetpack Compose",
        "summary": "Android developer with 4 years shipping apps to millions of users. Expert in Kotlin, Compose, and offline-first architecture.",
        "skills": ["Kotlin", "Android", "Jetpack Compose", "Room", "Retrofit", "MVVM", "Coroutines", "Firebase", "Git"],
        "total_experience_years": 4.0,
        "work_history": [
            {"company": "Swiggy", "title": "Android Developer", "duration_months": 30, "description": "Built delivery partner app used by 200K+ delivery executives."},
            {"company": "Nykaa", "title": "Junior Android Developer", "duration_months": 18, "description": "E-commerce app features and performance optimization."}
        ],
        "education": [{"degree": "B.Tech", "field": "Electronics & CS", "institution": "RVCE Bangalore"}],
        "activity": {"github_active": True, "open_source_contributions": 7, "blog_posts": 2, "last_active_days_ago": 20, "certifications_recent": 1},
        "location": "Bangalore, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C015",
        "name": "Tarun Verma",
        "headline": "Cybersecurity Engineer | Penetration Testing & SOC",
        "summary": "Security engineer with 6 years in penetration testing and security operations. CEH and OSCP certified.",
        "skills": ["Penetration Testing", "Python", "Kali Linux", "Burp Suite", "SIEM", "Splunk", "Network Security", "Incident Response"],
        "total_experience_years": 6.0,
        "work_history": [
            {"company": "Tata Communications", "title": "Senior Security Engineer", "duration_months": 36, "description": "Red team exercises and SOC operations for 50+ enterprise clients."},
            {"company": "Deloitte India", "title": "Security Consultant", "duration_months": 30, "description": "Pen testing engagements across BFSI sector."}
        ],
        "education": [{"degree": "B.Tech", "field": "Information Security", "institution": "Symbiosis Institute of Technology"}],
        "activity": {"github_active": True, "open_source_contributions": 11, "blog_posts": 8, "last_active_days_ago": 25, "certifications_recent": 2},
        "location": "Pune, India",
        "expected_role_level": "senior"
    },
    {
        "candidate_id": "C016",
        "name": "Pooja Shetty",
        "headline": "Generative AI Engineer | RAG & LLM Applications",
        "summary": "Gen AI engineer building RAG pipelines and LLM-powered products for 2 years. Expert in LangChain and vector databases.",
        "skills": ["Python", "LangChain", "LlamaIndex", "FAISS", "ChromaDB", "OpenAI", "HuggingFace", "FastAPI", "RAG"],
        "total_experience_years": 2.0,
        "work_history": [
            {"company": "Kore.ai", "title": "Generative AI Engineer", "duration_months": 24, "description": "Built enterprise RAG systems for HR and legal document Q&A."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "Manipal Institute of Technology"}],
        "activity": {"github_active": True, "open_source_contributions": 22, "blog_posts": 14, "last_active_days_ago": 2, "certifications_recent": 4},
        "location": "Hyderabad, India",
        "expected_role_level": "junior"
    },
    {
        "candidate_id": "C017",
        "name": "Aditya Kumar",
        "headline": "Blockchain Developer | Solidity & Web3",
        "summary": "Blockchain developer with 3 years building DeFi protocols and NFT marketplaces. Strong Solidity and Ethereum ecosystem skills.",
        "skills": ["Solidity", "Ethereum", "Web3.js", "Hardhat", "React", "Node.js", "IPFS", "Smart Contracts", "DeFi"],
        "total_experience_years": 3.0,
        "work_history": [
            {"company": "CoinDCX", "title": "Blockchain Developer", "duration_months": 24, "description": "Built DeFi yield farming protocol on Polygon."},
            {"company": "WazirX", "title": "Junior Web3 Developer", "duration_months": 12, "description": "NFT marketplace smart contracts."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "Thapar University"}],
        "activity": {"github_active": True, "open_source_contributions": 16, "blog_posts": 5, "last_active_days_ago": 9, "certifications_recent": 2},
        "location": "Delhi, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C018",
        "name": "Ritu Agarwal",
        "headline": "QA Automation Engineer | Selenium & Cypress",
        "summary": "QA automation engineer with 5 years building test frameworks. Expert in API and UI test automation.",
        "skills": ["Selenium", "Cypress", "Python", "Java", "REST API Testing", "Postman", "Jenkins", "JIRA", "BDD"],
        "total_experience_years": 5.0,
        "work_history": [
            {"company": "Zoho", "title": "QA Automation Engineer II", "duration_months": 36, "description": "Built end-to-end test suite for CRM product with 10K test cases."},
            {"company": "HCL Technologies", "title": "QA Engineer", "duration_months": 24, "description": "Manual and automated testing for telecom client."}
        ],
        "education": [{"degree": "B.E.", "field": "Computer Science", "institution": "Anna University"}],
        "activity": {"github_active": True, "open_source_contributions": 4, "blog_posts": 2, "last_active_days_ago": 35, "certifications_recent": 1},
        "location": "Chennai, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C019",
        "name": "Sandeep Mishra",
        "headline": "Data Analyst | Power BI & SQL Reporting",
        "summary": "Data analyst with 3 years creating business dashboards and insights reports for retail and supply chain.",
        "skills": ["SQL", "Power BI", "Excel", "Python", "Data Visualization", "Statistics", "Tableau", "ETL"],
        "total_experience_years": 3.0,
        "work_history": [
            {"company": "Reliance Retail", "title": "Data Analyst", "duration_months": 30, "description": "Built supply chain analytics dashboards for 1500+ stores."},
            {"company": "Genpact", "title": "Business Analyst", "duration_months": 12, "description": "Data reporting for insurance client."}
        ],
        "education": [{"degree": "B.Com", "field": "Statistics", "institution": "Delhi University"}],
        "activity": {"github_active": False, "open_source_contributions": 0, "blog_posts": 1, "last_active_days_ago": 60, "certifications_recent": 1},
        "location": "Delhi, India",
        "expected_role_level": "mid"
    },
    {
        "candidate_id": "C020",
        "name": "Kavitha Subramaniam",
        "headline": "Site Reliability Engineer | SRE & Observability",
        "summary": "SRE with 7 years ensuring 99.99% uptime for large-scale distributed systems. Expert in incident management and chaos engineering.",
        "skills": ["SRE", "Python", "Go", "Kubernetes", "Prometheus", "Grafana", "Terraform", "Chaos Engineering", "PagerDuty"],
        "total_experience_years": 7.0,
        "work_history": [
            {"company": "Ola Electric", "title": "Senior SRE", "duration_months": 30, "description": "Led reliability engineering for EV charging platform."},
            {"company": "Myntra", "title": "SRE Engineer", "duration_months": 36, "description": "Built observability stack for e-commerce platform."}
        ],
        "education": [{"degree": "B.Tech", "field": "Computer Science", "institution": "PSG Tech Coimbatore"}],
        "activity": {"github_active": True, "open_source_contributions": 19, "blog_posts": 10, "last_active_days_ago": 11, "certifications_recent": 2},
        "location": "Bangalore, India",
        "expected_role_level": "senior"
    }
]
