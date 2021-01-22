# Http

# Methods
* GET: everything included in URL, good for bookmarking and navigating back
* POST: more secure since post data not bookmarked and back button does not again send data with post body
* HEAD: same way as GET but except that the server should not return a message body. Use case: checking if a resource is present before executing GET
* TRACE: designed for diagnostic purposes. Server returns in response body the exact content of the request message it received. This can be use to detect the effoct of any proxy servers between client and server.
* OPTION: ask to server to report the available HTTP Methods (f.e.: GET, POST, etc.)
* PUT: Attempts to upload a specific resource to the server. if enabled might be able to upload a script
* any many more methods