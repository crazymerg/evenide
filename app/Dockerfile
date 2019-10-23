FROM ruby:2.6.3 as build

LABEL service="even-number-checker"

RUN mkdir -p /opt/even-number-checker
WORKDIR /opt/even-number-checker

COPY . /opt/even-number-checker
RUN bundle install

FROM ruby:2.6.3-alpine3.10
COPY --from=build /usr/local/bundle /usr/local/bundle

WORKDIR /opt/even-number-checker
COPY . /opt/even-number-checker

CMD ["ruby", "app.rb"]
