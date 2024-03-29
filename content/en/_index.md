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
        filename: welcome.jpg
      cta:
        label: 'Get in touch'
        url: /contact/
      cta_alt:
        label: 'Meet the Team'
        url: /people/
      text: |

        <br>
          Led by Dr Anna Moles, the Tissue Remodelling, Fibrosis and Cancer group has a transversal approach to science, with an enthusiastic and highly skilled team of researchers that enjoy doing science together and learning from each other every day.
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
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: title_bg.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
