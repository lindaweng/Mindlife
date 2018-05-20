require 'bundler'
Bundler.require
require "sinatra"
require "./models.rb"
require 'pycall/import'

class MyApp < Sinatra::Base
    get '/' do
       erb :index
    end
    
    get '/chatBot' do
        @num = 0
        @history = ""
        erb :chatBot
    end
    
    get '/survey' do
        erb :survey
    end
    
    post '/ask' do
        question = params[:message]
        @num = params[:messageNum].to_i
        @history = params[:history]
        answer = getAnswer(@num)
        @num += 1
        @history += "\n" + question
        @history += "\n" + answer
        erb :chatBot
    end
    
    post '/submit' do
        ans1 = params[:ans1]
        ans2 = params[:ans2]
        ans3 = params[:ans3]
        ans4 = params[:ans4]
        ans5 = params[:ans5]
        ans6 = params[:ans6]
        ans7 = params[:ans7]
        ans8 = params[:ans8]
        ans9 = params[:ans9]
        ans10 = params[:ans10]
        ans = ans1 + "$" + ans2 + "$" + ans3 + "$" + ans4 + "$" + ans5 + "$" + ans6 + "$" + ans7 + "$" + ans8 + "$" + ans9 + "$" + ans10
        puts ans
        # @diagnosis = `python models2.py ans`
        # PyCall.exec('from sys import argv')
        # PyCall.exec('python print "Your first variable is called ", argv[1]')
        # @diagnosis = `python models2.py argv[1]`
        @diagnosis = "Persistent depressive disorder. Formerly called dysthymia, this type of depression refers to low mood that has lasted for at least two years but may not reach the intensity of major depression. Many people with this type of depression type are able to function day to but feel low or joyless much of the time. Some depressive symptoms, such as appetite and sleep changes, low energy, low self-esteem, or hopelessness, are usually part of the picture. Please see a professional mental health professional."
        erb :diagnosis
    end
    
    get '/comics' do
        erb :comics
    end
    

end