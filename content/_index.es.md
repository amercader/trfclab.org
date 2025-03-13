---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Laboratorio de Remodelación Tisular, Fibrosis y Cáncer
      image:
        filename: welcome2.jpg
      cta:
        label: 'Contacta'
        url: /contact/
      cta_alt:
        label: "Conoce al equipo"
        url: /people/
      text: |
        <br>
        Liderado por la Doctora Anna Moles, el grupo de Remodelación Tisular, Fibrosis y Cáncer tiene un enfoque científico transversal, con un equipo puntero de investigadores que trabaja con las técnicas más avanzadas.
        <br/>

  - block: collection
    content:
      title: Líneas de investigación
      text:
      count: 4
      offset: 0
      order: desc
      page_type: lines
    design:
      view: showcase2
      columns: '1'

  - block: collection
    content:
      title: Noticias
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
