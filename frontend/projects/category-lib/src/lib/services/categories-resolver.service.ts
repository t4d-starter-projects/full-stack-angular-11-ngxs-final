import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

import { Category } from '../models/Category';
import { CategoriesService } from './categories.service';

@Injectable({
  providedIn: 'root'
})
export class CategoriesResolverService implements Resolve<Category[]> {

  constructor(private categoriesSvc: CategoriesService) { }

  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot):
    Category[] | Observable<Category[]> | Promise<Category[]> {

    return this.categoriesSvc.all();
  }
}
