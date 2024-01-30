relative_point = 6

start_sentence = ('Would you like to decide about work, application or other? Please select 0 for job, 1 for application'
                  'or any other number for general decision.')

error_string = 'You inserted a character, not an integer. Please restart.'

########################################JOB/CAREER############################################

trade_factors_job = [{
    'name': 'Company',
    'description': 'Ranking and prestige of the company.',
    'weight absolute': 7,
    'weight relative': 4
    },
    {
    'name': 'Perspective of Career',
    'description': 'Doors that will be open to you after the job. Which companies are doing similar stuff?',
    'weight absolute': 7,
    'weight relative': 7
    },
    {
    'name': 'Contribution to Industry',
    'description': 'How big is the impact of your work on the Space Industry?',
    'weight absolute': 9,
    'weight relative': 7
    },
    {
    'name': 'Daily Activities',
    'description': 'How much would you enjoy the daily tasks? How much thinking is required? Excited to go to work?',
    'weight absolute': 9,
    'weight relative': 8
    },
    {
    'name': 'Team',
    'description': 'How friendly and open minded are the people? How easily can you make friends?',
    'weight absolute': 8,
    'weight relative': 5
    },
    {
    'name': 'Work Environment',
    'description': 'How much excited are you to join the company and go to the office? Equipment? Location?',
    'weight absolute': 6,
    'weight relative': 3
    },
    {
    'name': 'Payment',
    'description': 'How much are you getting paid in this job w.r.t other positions?',
    'weight absolute': 5,
    'weight relative': 2
    },
    {
    'name': 'Balance life work',
    'description': 'Can you still cultivate passions and relationships? To which degree the job gets into your life?',
    'weight absolute': 9,
    'weight relative': 8
    },
    {
    'name': 'Personal Growth',
    'description': 'How much do you expect to grow in this job? How many skills will you learn? To which depth?',
    'weight absolute': 10,
    'weight relative': 10
    }
]

sum = 0
total = relative_point * len(trade_factors_job)
for i in trade_factors_job:
    sum += i['weight relative']
print(total, sum)