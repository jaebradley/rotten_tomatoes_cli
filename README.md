# Rotten Tomatoes CLI

## Install
`pip install rotten_tomatoes_cli`

## Search

`rotten search {term}`

### Harry Potter Example

`rotten search "Harry Potter"`

![alt-text](http://imgur.com/MNAwVxI.png)

### Master of None Example

`rotten search "Master of None"`

![alt-text](http://imgur.com/FNPejbR.png)

## Browse

### TV

`rotten browse tv {category}`

Category Argument
* `new` (default)
* `popular`
* `fresh`

#### Browse Popular TV Shows Example

`rotten browse tv popular`

![alt-text](http://imgur.com/3PYkLuz.png)

### Movies

Options:
* `--minimum_rating` / `-l`
  * Minimum allowable Rotten Tomatoes score
  * Default: `70`
* `--maximum_rating` / `-h`
  * Maximum allowable Rotten Tomatoes score
  * Default: `100`
* `--certified_fresh` / `-f`
  * Boolean flag that represents whether or not to only show "Certified Fresh" movies
  * Default: `True`
* `--service` / `-s`
  * Filter by specified streaming services
  * Default: All services
  * Can specify multiple services
  * Values:
    * `amazon`
    * `prime`
    * `hbo`
    * `itunes`
    * `netflix`
    * `vudu`
    * `fandango`
* `--genre` / `-g`
  * Filter by specified genres
  * Default: All genres
  * Can specify multiple genres
  * Values:
    * `action`
    * `animation`
    * `art_and_foreign`
    * `classics`
    * `comedy`
    * `documentary`
    * `drama`
    * `horror`
    * `family`
    * `mystery`
    * `romance`
    * `scifi`
* `--sort_by`
  * Sort results by specified value
  * Default: `popularity`
  * Values:
    * `popularity`
    * `release`


#### Streaming

`rotten browse movies streaming {category}`

Category Argument
* `new` (default)
* `all`
* `top`
* `upcoming`
* `fresh`

##### Upcoming Movies on Netflix or Amazon Prime with a minimum rating of 90

`rotten browse movies streaming upcoming -l 90 -s netflix -s prime`

![alt-text](http://imgur.com/7aP33au.png)

#### Theaters

`rotten browse movies theaters {category}`

Category Argument
* `opening` (default)
* `playing`
* `upcoming`
* `fresh`

##### Action Movies in Theaters with a minimum rating of 90

`rotten browse movies theaters playing -l 90 -g action`

![alt-text](http://imgur.com/vU54rQr.png)
