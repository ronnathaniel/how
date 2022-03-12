# how.

> How do I ...?
>
> This project was started to help developers ask more questions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Foss](#foss)
- [Community](#community)
- [Contributors](#contributors)
- [Copyright](#copyright)




## Installation

Install **using pypi**  -->

    $ pip3 install askquestions
    
Or **git** -->

    $ pip3 install git+https://github.com/ronnathaniel/how
    
Or **from source** -->

    $ git clone https://github.com/ronnathaniel/how.git
    $ cd how
    $ pip3 install .

## Usage

    $ how QUERY*

Ask your terminal directly.

    $ how do i exit vim
    ➜       ...
    ➜       ...

Optional Arguments

**shorthand**|**longhand**|**type**|**default**|**description**
:-----:|:-----:|:-----:|:-----:|:-----:
-n|--num|int|5|Amount of links to return
-g|--google|-|False|If exists
-s|--sites|comma-sep list| stackoverflow.com| sites to check for using google.com
    
And have fun.

    $ how -n 10 -s youtube.com,stackoverflow.com,example.com exit vi
    
    Results from youtube.com:
    ➜       ...
    ➜       ...
   
    Results from stackoverflow.com:
    ➜       ...
    ➜       ...
    
    Results from example.com:
    None found.
    If a discrepency is found ➜ contact the team at rnathaniel7@gmail.com.

## FOSS 

[`googlesearch-python`](https://pypi.org/project/googlesearch-python/) - "A Python library for scraping the Google search engine."


## Community

We want to build a community of question-askers.

After all, it is only when we ask questions that we can learn anything.

Contributions are more than welcome, maintainers are always invited, and if you can ask questions you're a VIP.

## Contributors

[![](https://github.com/ronnathaniel.png?size=50)](https://github.com/ronnathaniel)  [![](https://github.com/itaybachar.png?size=50)](https://github.com/itaybachar)
## Copyright

MIT License. 

All rights reserved.

![a-dead-poets-society](https://cdn.quotesgram.com/img/59/18/595506754-m_1918662_hxtIlAK3iZaf.jpg)

end.