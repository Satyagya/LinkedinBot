# General bot settings

# browser you want the bot to run ex: ["Firefox"], ["Chrome"] choose one only
browser = ["firefox"]
# Optional! run browser in headless mode, no browser screen will be shown it will work in background.
headless = False
# Optional! for Firefox enter profile dir to run the bot without logging in your account each time
firefoxProfileRootDir = r""
# If you left above field empty enter your Linkedin password and username below
# Linkedin credits
email = ""
password = ""

# These settings are for running Linkedin job apply bot
LinkedinBotProPasswrod = ""
# location you want to search the jobs - ex : ["Poland", "Singapore", "New York City Metropolitan Area", "Monroe County"]
# continent locations:["Europe", "Asia", "Australia", "NorthAmerica", "SouthAmerica", "Africa", "Australia"]
location = ["Bengaluru, Karnataka, India"]
# keywords related with your job search
keywords = ["Software Engineer"]
# keywords = ["programming"]
#job experience Level - ex:  ["Internship", "Entry level" , "Associate" , "Mid-Senior level" , "Director" , "Executive"]
experienceLevels = ["Entry level" , "Associate" , "Mid-Senior level"]
#job posted date - ex: ["Any Time", "Past Month" , "Past Week" , "Past 24 hours"] - select only one
datePosted = ["Past 24 hours"]
# datePosted = ["Past 24 hours"]
#job type - ex:  ["Full-time", "Part-time" , "Contract" , "Temporary", "Volunteer", "Intership", "Other"]
jobType = ["Full-time", "Part-time" , "Contract"]
#remote  - ex: ["On-site" , "Remote" , "Hybrid"]
remote = ["On-site" , "Remote" , "Hybrid"]
#salary - ex:["$40,000+", "$60,000+", "$80,000+", "$100,000+", "$120,000+", "$140,000+", "$160,000+", "$180,000+", "$200,000+" ] - select only one
salary = [ ""]
#sort - ex:["Recent"] or ["Relevent"] - select only one
sort = ["Relevent"]
#Follow companies after sucessfull application True - yes, False - no
followCompanies = True
# your country code for the phone number - ex: fr
country_code = "in"
# Your phone number without identifier - ex: 123456789
phone_number = "8171495766"



# Words which if are present, the jobs won't be applied to
filter_words = ["mobile", "react", "test", "angular", "frontend", "senior", "sr", "principal", "staff", "lead", "firmware", "data", "android", "ios", "devops"]

# Words which if are present, then only the jobs will be applied to
target_words = ["java", "software", "backend"]

