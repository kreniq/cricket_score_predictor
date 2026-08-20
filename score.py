def score():
    run_rate=runs/done_overs
    print('current run-rate is:',run_rate)
    overs_left=total_overs-done_overs
    predicted_score=runs+(run_rate*overs_left)
    print('predicted score is:',predicted_score)
    if wickets<=2:
        Wicket_adjusted_scoring_rate=run_rate*1.05
    elif wickets<=5:
        Wicket_adjusted_scoring_rate=run_rate*0.95
    elif wickets<=8:
        Wicket_adjusted_scoring_rate=run_rate*0.80
    else:
        Wicket_adjusted_scoring_rate=run_rate*0.60
    print('required Wicket-adjusted scoring rate for chasing team is:',Wicket_adjusted_scoring_rate)
    if chase:
        runs_needed=target_runs-runs
        required_runrate=runs_needed/overs_left
        print('required run-rate is:',required_runrate )
    else:
        print('no required run-rate for team batting first')


chase=input('team is chasing:(yes/no)').lower()=='yes'
runs=int(input('enter current score:'))
done_overs=int(input('enter overs completed:'))
wickets=int(input('enter wickets lost:'))
total_overs=int(input('enter total overs:'))
if chase:
    target_runs=int(input('enter the runs made by team batting first:'))
score()
