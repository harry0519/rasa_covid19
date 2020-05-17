## PERSONA: people from China ask for covid-19 situation 
* greet
  - utter_greet
* ask_covid19_situation_china
  - form{"name":"covid_situation_form"}
  - form{"name":null}
  - action_query_situation
  - utter_ask_solve_the_problem
* affirm{"Resolve_results":"Yes"}
  - utter_confirmed_then_continue_topic
* goodby
  - utter_goodbye
  - action_renew


## say hello
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

