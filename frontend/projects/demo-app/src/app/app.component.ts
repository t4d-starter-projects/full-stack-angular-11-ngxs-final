import { Component } from '@angular/core';

import { isNil } from 'lodash-es';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'demo-app';

  constructor() {

    if (isNil(null)) {
      console.log('is null');
    }

  }
}
