console.log("Javascript fully loaded properly");

/**
*	Description: Contain the main functionality of the entire project in JS code through the use of Angular JS
*		Angular JS lets us have the ability to shift our Server Side functionality to the Front End
*		So long as we keep the sensitive information on the server, and not here, this is perfectly acceptable
*
*	File: 					MyScript.js
*	Author: 				Wesley Couturier
*	Date (last modified): 	11-7-2016 (mm-dd-yyyy)
*/

// The ONLY globals we will have.
var app = angular.module("myApp", []);

// Service contains variables and functions that multiple controllers might need access to.
// You can only get access to service variables through the use of it's functions, a.k.a. Encapsulation.
app.service('activeTabs', function() {
	// IDs for the tabs that determine which tab is active, so we know where to post our tab content
	var myIDs = {
		"people": angular.element(document.querySelector('#People')),
		"places": angular.element(document.querySelector('#Places')),
		"purpose": angular.element(document.querySelector('#Purpose'))
	};

	// Bool to double check if we're allowed to get new content
	var reload = true;

	// Set/Dictionary used to contain the current contents of each tab. Why make another query when we had
	// it before?
	var myJobs = {
		"programming": "",
		"writing": "",
		"all": ""
	};

	return {
		// Returns specified set/Dictionary
		getJobBoard: function(idToGet) {
			var temp = Object.keys(myJobs);
			for (var i = 0; i < temp.length; i++) {
				if (angular.equals(temp[i], idToGet)) {
					return myJobs[temp[i]];
				}
			}
		},
		// Sets specified set/Dictionary in the Service
		setJobBoard: function(idToChange, myJson) {
			var temp = Object.keys(myJobs);
			for (var i = 0; i < temp.length; i++) {
				if (angular.equals(temp[i], idToChange)) {
					myJobs[temp[i]] = myJson;
				}
			}
		},

		getReload: function() {
			return reload;
		},

		setReload: function(boolIn) {
			reload = boolIn;
		},

		getIDs: function() {
			return myIDs;
		},
		// If we want to know which tab we're on, we need to check which one is active. This function
		// updates our service IDs so we know which one is active.
		updateIDs: function() {
			myIDs = {
				"programming": angular.element(document.getElementById('ProgrammingJobs')),
				"writing": angular.element(document.getElementById('WritingJobs')),
				"all": angular.element(document.getElementById('AllJobs'))
			};
		},

		reloadContainer: function() {
			// Need to make sure we get the right info for the right tab
			this.updateIDs();
			// tell parseString to remake url and Query
			reload = true;
			return this.getJobBoard();
		}
	};
});

url_builder = function(baseUrl, GivenJson) {
    /** This builds the api url for indeed's request
     *	PARAMETERS:
     *		baseUrl - the header url for indeed, typically is contained in $scope.indeedRequestUrl
     *		GivenJson - The JSON object that contains the different that are to be added to make the url
     * 	RETURNS:
     *		correctly built URL as a String
     */
    var urlToReturn = "";
    urlToReturn += baseUrl;
    for (var key in GivenJson) {
        if (GivenJson.hasOwnProperty(key)) { //THIS WORKS!!
            urlToReturn += key + "=" + GivenJson[key] + "&";
        }
    }
    return urlToReturn;
};

app.service('characterStuff', function($q, $http) {
	// IDs for the tabs that determine which tab is active, so we know where to post our tab content
	var myIDs = {
		"basic": angular.element(document.querySelector('#Basic')),
		"skills": angular.element(document.querySelector('#Skills')),
		"personal": angular.element(document.querySelector('#Personal'))
	};

	// Bool to double check if we're allowed to get new content
	var reload = true;

	// Set/Dictionary used to contain the current contents of each tab. Why make another query when we had
	// it before?
	var myJobs = {
		"basic": "",
		"skills": "",
		"personal": ""
	};

    this.url_builder = function(baseUrl, GivenJson) {
		/** This builds the api url for indeed's request
		 *	PARAMETERS:
		 *		baseUrl - the header url for indeed, typically is contained in $scope.indeedRequestUrl
		 *		GivenJson - The JSON object that contains the different that are to be added to make the url
		 * 	RETURNS:
 		 *		correctly built URL as a String
		 */
		var urlToReturn = "";
		urlToReturn += baseUrl;
		for (var key in GivenJson) {
			if (GivenJson.hasOwnProperty(key)) { //THIS WORKS!!
				urlToReturn += key + "=" + GivenJson[key] + "&";
			}
		}
		return urlToReturn;
	}

    this.makeUrl = function (requestURL, requestParams) {
		return url_builder(requestURL, requestParams);
	}

    this.URL_Handle = function(requestURL, requestParams) {
		/** Function gets built URL, then uses $http to request a response. We should have the
		*		functions built into $http for success or failure
		*	PARAMETERS:
		*		none
		* 	RETURNS:
		*		nothing
		*/
        var deferred = $q.defer();
		requestURL = url_builder(requestURL, requestParams);

		// For now, we must assume that we have a XML string to setup list-group stuff on the main page
		$http.get(requestUrl).then(function successCallback(response) {
	    // this callback will be called asynchronously
	    // when the response is available
		//return data.data;
        deferred.resolve(response.data);
	  	}, function errorCallback(response) {
	    // called asynchronously if an error occurs
	    // or server returns response with an error status.
		console.log("Error Occurred in char/dump call");
        deferred.reject("Error Occurred in char/dump call - " + response)
		});

        return deferred.promise;
	}

	return {
		// Returns specified set/Dictionary
		getJobBoard: function(idToGet) {
			var temp = Object.keys(myJobs);
			for (var i = 0; i < temp.length; i++) {
				if (angular.equals(temp[i], idToGet)) {
					return myJobs[temp[i]];
				}
			}
		},
		// Sets specified set/Dictionary in the Service
		setJobBoard: function(idToChange, myJson) {
			var temp = Object.keys(myJobs);
			for (var i = 0; i < temp.length; i++) {
				if (angular.equals(temp[i], idToChange)) {
					myJobs[temp[i]] = myJson;
				}
			}
		},

        getURLStuff: function (reqUrl, reqParams) {
            var deferred = $q.defer();
    		var requestURL = url_builder(reqUrl, reqParams);

    		// For now, we must assume that we have a XML string to setup list-group stuff on the main page
    		$http.get(requestURL).then(function successCallback(response) {
    	    // this callback will be called asynchronously
    	    // when the response is available
    		//return data.data;
            deferred.resolve(response.data);
    	  	}, function errorCallback(response) {
    	    // called asynchronously if an error occurs
    	    // or server returns response with an error status.
    		console.log("Error Occurred in char/dump call");
            deferred.reject("Error Occurred in char/dump call - " + response)
    		});

            return deferred.promise;
            //console.log(typeof(this.URL_Handle));
            //return this.URL_Handle(reqUrl, reqParams);
        },

		getIDs: function() {
			return myIDs;
		}
	};
});

// Parent Controller used to take broadcast event and data from one child to another
app.controller("tabParent", function($scope, activeTabs, $sce) {
    // Nothing for right now
});

// Controller used to broadcast to sibling controller to update tab content
app.controller("myCtrl", function($scope, $http, activeTabs) {
	$scope.getUpdate = function($event) {
		// This will call the "url_reload_check_two" function in Parent to give this controller's
		// sibling the tab we seleted.
		$scope.$parent.$broadcast("url_reload_check_two", $event.target.hash);
	};
});

// Controller that handles the tab content, url building and querying from Indeed's API
app.controller("parseString", function($scope, $sce, $http, activeTabs) {
	// NEED variable of this instance. You'll see later.
	var vm = this;
	// Which tab ID is Active for tab content load.
	var currentId = "";
	// Empty container for response returns.
	vm.response = [];

	$scope.requestURL = "/char/dump/?";
	$scope.requestParams = {
		"cid": 1,
	};

	$scope.url_builder = function(baseUrl, GivenJson) {
		/** This builds the api url for indeed's request
		 *	PARAMETERS:
		 *		baseUrl - the header url for indeed, typically is contained in $scope.indeedRequestUrl
		 *		GivenJson - The JSON object that contains the different that are to be added to make the url
		 * 	RETURNS:
 		 *		correctly built URL as a String
		 */
		var urlToReturn = "";
		urlToReturn += baseUrl;
		for (var key in GivenJson) {
			if (GivenJson.hasOwnProperty(key)) { //THIS WORKS!!
				urlToReturn += key + "=" + GivenJson[key] + "&";
			}
		}
		return urlToReturn;
	};

	$scope.makeUrl = function () {
		$scope.requestURL = $scope.url_builder($scope.requestURL, $scope.requestParams);
		console.log($scope.requestURL);
	}

	$scope.URL_Handle = function() {
		/** Function gets built URL, then uses $http to request a response. We should have the
		*		functions built into $http for success or failure
		*	PARAMETERS:
		*		none
		* 	RETURNS:
		*		nothing
		*/
		makeUrl();

		// For now, we must assume that we have a XML string to setup list-group stuff on the main page
		$http.get($scope.requestUrl).then(function successCallback(response) {
	    // this callback will be called asynchronously
	    // when the response is available
		vm.response = data.data;
		console.log(vm.response);
	  	}, function errorCallback(response) {
	    // called asynchronously if an error occurs
	    // or server returns response with an error status.
		console.log("Error Occurred in char/dump call");
		});
	};

	// Some defaults to get the ball rolling.
	currentId = "People";
});

app.controller("characterBuild", function($scope, characterStuff) {

	$scope.requestURL = "/char/dump/?";
	$scope.requestParams = {
		"cid": 1,
	};

    characterStuff.getURLStuff($scope.requestURL, $scope.requestParams).then(function(data){
        console.log("SUCCESS");
        console.log(data);
    }, function(data){
        console.log("FAILED - " + data)
    });

    //characterStuff.getURLStuff($scope.requestURL, $scope.requestParams);
});
