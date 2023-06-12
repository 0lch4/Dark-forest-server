`admin/` - main django admin panel

`stats/create_user` - this endpoint is only accessed for client, here users create accounts

`stats/register_success` - this endpoint return information to the client when register ends successfully

`stats/register_fail` - this endpoint return information to the client when user can't create account for some resons

`stats/login` this endpoint is only accessed for client, here users login to the server

`stats/login_success` - this endpoint return information to the client when logged in ends successfully

`stats/login_fail` - this endpoint return information to the client when user can't logged in for some resons

`stats/modify_best_score` - this endpoint is only accessed for client, updates users best score

`stats/show_best_score` this endpoint return best scores from players

`stats/modify_stats` - this endpoint is only accessed for client, updates users stats

`stats/show_stats` this endpoint return stats from players