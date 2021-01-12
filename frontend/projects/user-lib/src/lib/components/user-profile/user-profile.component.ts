import { Component, OnInit, Input } from '@angular/core';

import { UserProfile } from '../../models/UserProfile';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {

  @Input()
  public userProfile: UserProfile | null = null;

  constructor() { }

  ngOnInit(): void {
  }

}
