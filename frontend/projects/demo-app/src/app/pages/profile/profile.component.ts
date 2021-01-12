import { Component, OnInit } from '@angular/core';
import { Select } from '@ngxs/store';
import { Observable } from 'rxjs';

import { UsersService } from '@t4d-wnow/user-lib';
import { ChangePasswordForm } from '@t4d-wnow/user-lib';

import { CurrentUserState } from '@t4d-wnow/user-lib';


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  @Select((state: { currentUser: CurrentUserState }) => state.currentUser)
  public currentUser$: Observable<CurrentUserState> | undefined;

  constructor(public usersSvc: UsersService) { }

  ngOnInit(): void {
  }

  public doChangePassword(changePasswordForm: ChangePasswordForm) {
    const { username, userKind } = this.usersSvc.getCurrentUser()!;

    this.usersSvc.changePassword(
      username, userKind,
      changePasswordForm.currentPassword,
      changePasswordForm.newPassword).subscribe();
  }

}
