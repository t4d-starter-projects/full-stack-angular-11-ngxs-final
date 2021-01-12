import { Injectable } from '@angular/core';
import {
  ActivatedRouteSnapshot, CanActivate,
  RouterStateSnapshot, UrlTree, Router
} from '@angular/router';
import { Observable } from 'rxjs';

import { UsersService } from './users.service';

@Injectable({
  providedIn: 'root'
})
export class LoggedInGuardService implements CanActivate {

  constructor(private usersSvc: UsersService, private router: Router) { }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot):
    boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {

      if (!this.usersSvc.getCurrentUser()) {
        return this.router.parseUrl('/login');
      } else {
        return true;
      }

  }
}
