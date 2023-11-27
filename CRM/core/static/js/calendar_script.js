const calendar = document.querySelector(".calendar"),
  date = document.querySelector(".date"),
  daysContainer = document.querySelector(".days"),
  prev = document.querySelector(".prev"),
  next = document.querySelector(".next"),
  todayBtn = document.querySelector(".today-btn"),
  gotoBtn = document.querySelector(".goto-btn"),
  dateInput = document.querySelector(".date-input"),
  eventDay = document.querySelector(".event-day"),
  eventDate = document.querySelector(".event-date"),
  eventsContainer = document.querySelector(".events"),
  addEventBtn = document.querySelector(".add-event"),
  addEventWrapper = document.querySelector(".add-event-wrapper "),
  addEventCloseBtn = document.querySelector(".close ");

let today = new Date();
let activeDay;
let month = today.getMonth();
let year = today.getFullYear();

const months = [
  "Enero",
  "Febrero",
  "Marzo",
  "Abril",
  "Mayo",
  "Junio",
  "Julio",
  "Agosto",
  "Septiembre",
  "Octubre",
  "Noviembre",
  "Diciembre",
];

const days = [
  "Dom",
  "Lun",
  "Mar",
  "Mié",
  "Jue",
  "Vie",
  "Sáb"
];

const filteredEvents=[];
let eventsArr=[];
getEvents()


//function to add days in days with class day and prev-date next-date on previous month and next month days and active on today
function initCalendar() {
  fetch('/event/calendar/events')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    eventsArr=data

    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const prevLastDay = new Date(year, month, 0);
    const prevDays = prevLastDay.getDate();
    const lastDate = lastDay.getDate();
    const day = firstDay.getDay();
    const nextDays = 7 - lastDay.getDay() - 1;

    date.innerHTML = months[month] + " " + year;

    let days = "";

    // Add the names of the days in Spanish
    for (let i = 0; i < days.length; i++) {
      days += `<div class="day day-name">${days[i]}</div>`;
    }

    for (let x = day; x > 0; x--) {
      days += `<div class="day prev-date">${prevDays - x + 1}</div>`;
    }

    for (let i = 1; i <= lastDate; i++) {
      //check if event is present on that day
      let event = false;
      
      //console.log(eventsArr)
      eventsArr.forEach((eventObj) => {
        const given_date = getFormattedDate(year, month, i);
        //console.log("Lo de las fechas")
        //console.log(given_date)
        //console.log(eventObj.date)
        if (
          eventObj.date === given_date
        ) {
          event = true;
        }
      });

      //console.log("Lo de las fechas")
      //console.log(event)

      /*console.log("Lo de las fechas")
      console.log(new Date().getDate())
      console.log(new Date().getFullYear())
      console.log(new Date().getMonth())
      given_date=(new Date().getFullYear())+"-"+(new Date().getMonth())+"-"+(new Date().getDate())*/
      if (
        i === new Date().getDate() &&
        year === new Date().getFullYear() &&
        month === new Date().getMonth()
      ) {
        activeDay = i;
        getActiveDay(i);
        updateEvents(i);
        if (event) {
          days += `<div class="day today active event">${i}</div>`;
        } else {
          days += `<div class="day today active">${i}</div>`;
        }
      } else {
        if (event) {
          days += `<div class="day event">${i}</div>`;
        } else {
          days += `<div class="day ">${i}</div>`;
        }
      }
    }

    for (let j = 1; j <= nextDays; j++) {
      days += `<div class="day next-date">${j}</div>`;
    }
    daysContainer.innerHTML = days;
    addListner();
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
}

function prevMonth() {
  month--;
  if (month < 0) {
    month = 11;
    year--;
  }
  initCalendar();
}

function nextMonth() {
  month++;
  if (month > 11) {
    month = 0;
    year++;
  }
  initCalendar();
}

prev.addEventListener("click", prevMonth);
next.addEventListener("click", nextMonth);

initCalendar();

function addListner() {
  const days = document.querySelectorAll(".day");
  days.forEach((day) => {
    day.addEventListener("click", (e) => {
      getActiveDay(e.target.innerHTML);
      updateEvents(Number(e.target.innerHTML));
      activeDay = Number(e.target.innerHTML);
      days.forEach((day) => {
        day.classList.remove("active");
      });
      if (e.target.classList.contains("prev-date")) {
        prevMonth();
        setTimeout(() => {
          const days = document.querySelectorAll(".day");
          days.forEach((day) => {
            if (
              !day.classList.contains("prev-date") &&
              day.innerHTML === e.target.innerHTML
            ) {
              day.classList.add("active");
            }
          });
        }, 100);
      } else if (e.target.classList.contains("next-date")) {
        nextMonth();
        setTimeout(() => {
          const days = document.querySelectorAll(".day");
          days.forEach((day) => {
            if (
              !day.classList.contains("next-date") &&
              day.innerHTML === e.target.innerHTML
            ) {
              day.classList.add("active");
            }
          });
        }, 100);
      } else {
        e.target.classList.add("active");
      }
    });
  });
}

todayBtn.addEventListener("click", () => {
  today = new Date();
  month = today.getMonth();
  year = today.getFullYear();
  initCalendar();
});

dateInput.addEventListener("input", (e) => {
  dateInput.value = dateInput.value.replace(/[^0-9/]/g, "");
  if (dateInput.value.length === 2) {
    dateInput.value += "/";
  }
  if (dateInput.value.length > 7) {
    dateInput.value = dateInput.value.slice(0, 7);
  }
  if (e.inputType === "deleteContentBackward") {
    if (dateInput.value.length === 3) {
      dateInput.value = dateInput.value.slice(0, 2);
    }
  }
});

gotoBtn.addEventListener("click", gotoDate);

function gotoDate() {
  //console.log("here");
  const dateArr = dateInput.value.split("/");
  if (dateArr.length === 2) {
    if (dateArr[0] > 0 && dateArr[0] < 13 && dateArr[1].length === 4) {
      month = dateArr[0] - 1;
      year = dateArr[1];
      initCalendar();
      return;
    }
  }
  alert("Fecha Invalida");
}

function getActiveDay(date) {
  const day = new Date(year, month, date);
  const dayName = days[day.getDay()];
  eventDay.innerHTML = dayName;
  eventDate.innerHTML = date + " " + months[month] + " " + year;
}

function updateEvents(date) {
  //console.log(date)
  //console.log(month+1)
  //console.log(year)
  const given_date = getFormattedDate(year, month, date);
  //console.log(given_date)

  fetch('/event/calendar/events')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    eventsArr=data
    // Manejar los datos
    //console.log(data);

    sessionStorage.setItem('given_date', given_date);

    const filteredEvents = data.filter((event) => {
      return (
        given_date === event.date
      );
    });
    let events = "";
    //sessionStorage.setItem('status_event', 'CALENDAR');
    //console.log("Aqui van los eventos: ")
    //console.log(filteredEvents)
    if (filteredEvents.length > 0) {
      filteredEvents.forEach((event) => {
        events += `<div class="card">
        <h5 class="card-header">${event.name}</h5>
        <div class="card-body d-flex justify-content-between">
            <div>
                <h5 class="card-title">${event.type}</h5>
                <p class="card-text">${event.description}.</p>
            </div>
            <div class="text-right">
                <a href="/event/info/${event.id}" class="btn btn-success">Mas info</a>
                <a href="/event/delete/${event.id}" class="btn btn-danger">Borrar</a>
            </div>
        </div>
    </div>
    `;
      });
    } else {
      events = `<div class="no-event">
        <h3>Ningun evento</h3>
      </div>`;
    }
    
    eventsContainer.innerHTML = events;

  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
}

function getEvents() {
  fetch('/event/calendar/events')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    eventsArr=data
    return eventsArr
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
}


function getFormattedDate(year, month, day) {
  const formattedMonth = (month + 1).toString().padStart(2, '0'); // Asegura que tenga dos dígitos
  const formattedDay = day.toString().padStart(2, '0'); // Asegura que tenga dos dígitos
  return `${year}-${formattedMonth}-${formattedDay}`;
}
