# college-sentiment
NLP Sentiment analysis of comments pulled from various college review websites (i.e. "RateMyProf", "Unigo", "Reddit")

Kasey Castello
Hayes Neuman
Jacob Speicher
Sean Rice
Natural Language Processing Project Proposal

# Executive Summary
Many college students in the modern time go to the internet to express their emotion regarding their university and communicate with other students regarding issues on campus. These discussions exist on forums such as Reddit, Quora, and College Confidential and are an excellent resource to analyze camus culture. On the reverse side, every college student can remember the stressful time they endured while trying to decide which college they should attend. This time is often marked by extensive research through college forums to try to determine what life may be like on a given campus. While there is a dense supply of information present in forums, reading through hundreds of posts for each college one is considering attending is not feasible for the common student.


 This project aims to use sentiment analysis to allow students to quickly determine the percentage of posts for a given university that are positive, negative, and neutral, helping them to make their decision. Two models will be created based off of RateMyProfessor.com and Unigo.com. For each school a dataset of posts from each “official” school Reddit forum will be run through these sentiment analysis models to generate an overall sentiment. The two overall sentiments generated by the two models will be presented to the end user through the final website. The final deliverable will be a Lightweight Web Front-End using Python Flask that allows users to search for schools and get a report on their forum positivity.

# Goal 
The main goal of this project is to apply sentiment analysis methods to existing information present in university themed forums such as Reddit r/RPI or RateMyProfessor. The main feature of the product is its ability to scan a college forum to create a set of university-specific posts. For each post on the respective college forum, sentiment analysis approaches will be applied to determine the emotional tone of the post. The product will then calculate the percentage of posts that display positive, negative, and neutral sentiment for a given university. The final product will allow a user to search for universities and check the general feeling towards the institution. 

Students and university administrations can both benefit from the success of this project. This system will allow prospective students to get a general idea of whether students like their university or not, which could inform their decision of which university to attend. It also allows administrators to get a glimpse of how their students feel about their university, which might shepherd change. If a large portion of the student posts are negative, an administration might be easily able to gather this information and make changes to increase the positive sentiments felt by students.

# 1.3 Background and Motivation 
Almost everyone moving from high school to higher education has to go through a search process. In a lot of cases, it’s time consuming and difficult to find a school that the student feels would be a good fit for them for the next four or more years. Part of this search includes going to various review websites or forums for each school and sifting through numerous posts to find out current students opinions. With everything else a student has to do in their senior year from finding programs that fit to worrying about tuition and financial aid, this review/forum search could fall by the wayside. This project would make it a quick task to just navigate to a webpage and see an aggregate sentiment generated from reviews and forum posts. This would provide a useful metric when compared to an averaged score from 1 to 5 as most review websites will provide. The way that people write about their school will allow for better insight into the general atmosphere of the institution and make the college search just a little bit easier.

# System Architecture and Approach
There are three tasks to be completed for this project, namely creating sentiment analysis models, generating an overall sentiment for a school, and providing an interface for a user to access these sentiments. Firstly, two models will be created. One will be trained on data scraped from RateMyProfessor.com (there is a section for reviews of schools separate from reviews of professors), and the other from data scraped from Unigo.com. Then, for each school a dataset of posts from each “official” school Reddit forum will be run through these sentiment analysis models to generate an overall sentiment. The two overall sentiments generated by the two models will be presented to the end user through the final website. The website will be a simple page that will allow a user to navigate through a list of the currently available schools to see the overall sentiment.

# Deliverables 
Lightweight Web Front-End using Flask - 4/15
End user interface to search for schools.

# Time Table 
| Date      | Task                                                                                                                                         |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 3/11-3/18 | Scrape data from RateMyProfessor, Unigo, and Reddit                                                                                          |
| 3/19-3/25 | Determine structure of training data Discuss potential models Create train, test, and eval sets for RateMyProfessor.com and Unigo.com        |
| 3/26-4/1  | Create a model trained with data from RateMyProfessors.com happiness scores Create a model trained with data from Unigo.com happiness scores |
| 4/2-4/8   | Create Lightweight Web Front-End using Flask allowing users to view school data                                                              |
| 4/9-4/15  | Finish writing the report of the overall process, records, and findings Organize, create, and present the final presentation                 |
