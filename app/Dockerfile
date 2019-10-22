FROM ruby:alpine

RUN gem install sinatra

WORKDIR /usr/even_numbers
COPY . .

CMD ["ruby", "app.rb"]
