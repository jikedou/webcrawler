# coding:utf-8
import builtwith
import whois
testUrl='https://www.lagou.com/'
result=builtwith.parse(testUrl)
print "buildwith:",result
print whois.whois(testUrl)