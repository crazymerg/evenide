require 'sinatra'
require 'json'

set :port, 8080

get '/check_is_even/:number' do
    status 200
    result = (params['number'].to_i.even?) ?  true : false
    JSON.generate({:result => result})
end

get '/get_random_even/:range' do
  status 200
  (2..params['range'].to_i).step(2).to_a.shuffle.first.to_json
end
