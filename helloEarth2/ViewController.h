//
//  ViewController.h
//  helloEarth2
//
//  Created by Apple on 9/25/15.
//  Copyright © 2015 Michael Xu. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "WhirlyGlobeMaplyComponent/WhirlyGlobeComponent.h"
#import "ArticleScreenMarker.h"
#import "AnnotationView.h"
#import <CoreLocation/CoreLocation.h>

@interface ViewController : UIViewController
        <WhirlyGlobeViewControllerDelegate, MaplyViewControllerDelegate, CLLocationManagerDelegate>


@end

