"use strict";

angular.module('signal_app.hello', ['ngRoute'])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/menu', {
            templateUrl: "hello/hello.html",
            controller: "HelloCtrl"
        });
    }])
    .controller('HelloCtrl', ["$scope", "$location", "$http",
        function($scope, $location, $http) {
            $http.get("sample.json")
                .success(function (data, status, headers, config){
                    console.log(data);
                    $scope.data = data;
                });
    }]);
