require 'rack'
require 'rack/handler/puma'
require 'sinatra'
require 'sinatra/param'
require 'json'

class Api < Sinatra::Base
  helpers Sinatra::Param

  disable :show_exceptions
  disable :raise_errors
  disable :dump_errors

  before do
    content_type :json
  end

  get '/check_is_even/:number' do
    param :number, Integer, required: true

    body = {result: Integer(params['number']).even?}

    JSON.dump(status: 200, body: body)
  end

  get '/get_random_even' do
    param :min, Integer, required: true
    param :max, Integer, required: true

    random_even = loop do
      number = rand(Integer(params[:min])..Integer(params[:max]))
      break number if number.even?
    end

    JSON.dump(status: 200, body: {result: random_even})
  end
end

Rack::Handler::Puma.run(Api, :Port => 4567)
