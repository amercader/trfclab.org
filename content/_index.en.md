---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Tissue Remodeling, Fibrosis and Cancer Lab
      image:
        filename: welcome2.jpg
      cta:
        label: 'Get in touch'
        url: /contact/
      cta_alt:
        label: 'Meet the Team'
        url: /people/
      text: |

        <br>
        Welcome to the TRFC Lab!

        We are a group of highly motivated and passionate scientists working to better understand the cellular mechanisms controlling tissue remodelling, fibrosis and cancer.

        <br/>


  - block: collection
    content:
      title: Research lines
      text:
      count: 4
      offset: 0
      order: desc
      page_type: lines
    design:
      view: showcase2
      columns: '1'

      do_link: false

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      columns: '1'

---
