const pubSub = {
  events: {},
  subscribe(event, callback) {
    if (!this.events[event]) this.events[event] = []; // if no event, create it
    this.events[event].push(callback); // add callback to event
  },
};

pubSub.subscribe("update", (data) => console.log(data));
pubSub.publish("update", "some update");
