import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { UsersService } from '../../services/users.service';

@Component({
  selector: 'app-current-user',
  templateUrl: './current-user.component.html',
  styleUrls: ['./current-user.component.css']
})
export class CurrentUserComponent implements OnInit {

  get loggedIn(): boolean {
    return !!this.usersSvc.getCurrentUser();
  }

  get displayName(): string {
    return this.usersSvc.getCurrentUser()?.displayName ?? '';
  }

  get username(): string {
    return this.usersSvc.getCurrentUser()?.username ?? '';
  }

  constructor(private router: Router, private usersSvc: UsersService) { }

  ngOnInit(): void {
  }

  public navigateToProfile(): Promise<boolean> {
    return this.router.navigateByUrl('/profile');
  }

  public navigateToLogout(): Promise<boolean> {
    return this.router.navigateByUrl('/logout');
  }

  public navigateToLogin(): Promise<boolean> {
    return this.router.navigateByUrl('/login');
  }

}
