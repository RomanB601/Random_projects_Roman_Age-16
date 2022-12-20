from bs4 import BeautifulSoup
import requests
import time

def main():
    list,job = get_filtering()
    find_jobs(list,job)

def get_filtering(): #The input Method lets the user filter
    print("What job do you want to search for?")
    job = input(">")
    unfamiliar_skill_list = []
    print("Put some skill you aren't familiar with (type done when done)")
    while True:
        unfamiliar_skill = str(input(">")).strip()
        if unfamiliar_skill == "done":
            unfamiliar_skill_list.append("asdihasofhah134sihdfoiasdhiuh3iuhibig3u1ig2iiasgidgi2yg") 
            break
        unfamiliar_skill_list.append(unfamiliar_skill)
    print("Filtering out", end="")
    if len(unfamiliar_skill_list) == 1:
        print(" nothing", end="")
    elif len(unfamiliar_skill_list) == 2:
        print(f" {unfamiliar_skill_list[0]}", end="")
    elif len(unfamiliar_skill_list) == 3: 
        print(f" {unfamiliar_skill_list[0]} and {unfamiliar_skill_list[1]}", end="")
    else:
        for x in range(len(unfamiliar_skill_list)):
            if unfamiliar_skill_list[x] == "asdihasofhah134sihdfoiasdhiuh3iuhibig3u1ig2iiasgidgi2yg": continue
            elif x == (len(unfamiliar_skill_list)-2):
                print(f" and {unfamiliar_skill_list[x]}", end ="")
                break
            print(f" {unfamiliar_skill_list[x]},", end ="")
            
    print("... \n")
    return unfamiliar_skill_list, job


def find_jobs(unfamiliar_skill_list,job_choice): #does the webscraping and filtering
    t0 = time.time()
    unfamiliar_job_counter = 0
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_choice}&txtLocation=').text
    soup = BeautifulSoup(html_text, 'html5lib')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        counter_unfamilar_jobs = len(unfamiliar_skill_list)
        published_date = job.find('span', class_= 'sim-posted').text.strip()
        if "few" in published_date:
            company_name = job.find("h3", class_= 'joblist-comp-name').text.strip()
            skills = job.find('span', class_= 'srp-skills').text.strip().replace("  , ",",")
            for i in range(len(unfamiliar_skill_list)):
                if unfamiliar_skill_list[i].upper() not in skills.upper():
                    counter_unfamilar_jobs-=1
                elif unfamiliar_skill_list[i].upper() in skills.upper(): 
                    unfamiliar_job_counter+= 1/(len(unfamiliar_skill_list)-1)
                if unfamiliar_job_counter == (len(jobs)-1):
                    with open(f"posts/{index}.txt", 'w') as f:
                        f.write(f"No Jobs Found :(\n")
                    t1 = time.time()
                    total = t1-t0
                    print(f"File saved: {index}")
                elif unfamiliar_skill_list[i].upper() not in skills.upper() and counter_unfamilar_jobs == 0:
                    more_info = job.header.h2.a['href'] #Header goes into the job header its not a find method
                    with open(f'posts/{index}.txt', "w") as f: #f means file and w means write
                        f.write(f"Company Name: {company_name}\n")
                        f.write(f"Required Skills: {skills}\n")
                        f.write(f"Published Date: {published_date}\n")
                        f.write(f"More Info: {more_info}\n")
                    print(f"File saved: {index}")
        else: unfamiliar_job_counter +=1
    t1 = time.time()
    total = t1-t0
    print(f"Time:{total:.2f} seconds\n")
    return

if __name__ == "__main__":
    main()