FROM ruby:2.6.3 as builder

LABEL service="even-number-checker"

RUN mkdir -p /opt/even-number-checker
WORKDIR /opt/even-number-checker

COPY app/Gemfile.lock .
COPY app/Gemfile .
RUN bundle install

FROM ruby:2.6.3-alpine3.10
COPY --from=builder /usr/local/bundle /usr/local/bundle

WORKDIR /opt/even-number-checker
COPY app .

CMD ["ruby", "app.rb"]
