function getData(search)
{
  $.ajax({
    url: "/search",
    headers: {'X-CSRFToken': token},
    type: "POST",
    data: {
      search: search,
    },
    success: function(data)
    {
      let html = '';
      for (const row of data.persons){
        var url = "{% url 'anime' id=12345 nombre=54321 %}".replace(/12345/, row.slug).replace(/54321/, row.title);
        html += `
              <a href=${url} class="is-flex">
                <div class="column is-4-desktop is-2-mobile is-3-tablet">
                    <figure class="is-flex is-flex-direction-column is-justify-content-center is-align-items-center image" style="overflow: hidden;">
                        <img class="is-flex-shrink-0" style="min-width: 100%; min-height: auto; max-height: 100%; object-fit: cover;" src="{% url 'cover' size='small' filename='row.image' %}" alt="Placeholder image">
                    </figure>
                </div>
                <div class="column is-8-desktop is-8-mobile is-12-tablet is-flex is-flex-direction-column is-justify-content-center">
                    <div class="is-flex is-flex-direction-column">
                        <div class="is-flex">
                            <p class="title is-size-5-desktop is-size-5-tablet is-size-5-mobile" style="color:var(--main-text-color-hover); font-family: Montserrat; font-weight: 400; font-style:normal;">
                                ${row.title}
                            </p>
                        </div>
                        <!-- tipe -->
                        <div class="is-flex block">
                            <p class="subtitle is-size-5-desktop is-size-6-tablet is-size-7-mobile" style="color:var(--main-primary-color); font-family: Montserrat; font-weight: 400; font-style:normal;">
                                <span>
                                    ${row.tipo}
                                </span>
                            </p>
                        </div>

                    </div>
                </div>
                </a>
                <hr style="width: 100%;height:2px;border-width:0;background-color:var(--main-primary-color)">
        `;
      }
      $('#search-result').html(html);
    }
  });
}