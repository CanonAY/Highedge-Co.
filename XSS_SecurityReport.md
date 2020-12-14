### XSS Security Report

|      | Route/URL                      | Parameter   | XSS successful? |
|------|--------------------------------|-------------|-----------------|
| Scan | http://127.0.0.1:8081/sell     | sell-date   | No              |
|      | http://127.0.0.1:8081/update   | update-date | No              |
|      | http://127.0.0.1:8081/buy      | N/A         | No              |
|      | http://127.0.0.1:8081/         | password    | No              |
|      | http://127.0.0.1:8081/register | password    | No              |

Question 1:
- These two results are different because on the second scanninng we login to website with a valid user account and add the session id of that website, and thus it will have more scanning before we login and use the session id. The purpose to use session id is to ensure that the server identify the valid user account when it communicates with the web application (in this case login to the website). Such session id can also be used to hijack the current session and obtain potential privileges by an attacker. Thus session id will be updated frequently to avoid attacker's potentail attack.

Question 2:
- All the possible XSS links/routes covered in the table above. In the profile page, we provide user the link to /sell, /buy, and /update which are considered as vulnerable to XSS since all of these require user to input. When we use PwnXSS to scan, it had scanned all these links and none of these attack was successful. 