from jira import JIRA
jira = JIRA("https://12095.atlassian.net/",basic_auth=("harikapenumatsa942@gmail.com","ATATT3xFfGF0K9LoQz6aHfN2PXm1th0GFNbWOrojQ4XZgJUiz8ts7RhwUnkH_IOmkClNULOpyaIW4oT4BA00XVYT4skEDiNNuSLxR1i3EosxBljJ-CiCBIKRAJ56K3dZ64MsZxo1BHyys9yEF_sWQImQ0ywRJsI7tvy5HvezZq9Nd4X5llD-M9I=4A58FABC"))
project="Temperature"
new_issue=jira.search_issues("project= "+project,maxResults=500)
for issue in new_issue:
    print(issue,end="\n")
    print(issue.id,end="\n")
    print(issue.fields.issuetype,end="\n")